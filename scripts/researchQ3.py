import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
#BEGINYEAR
#ENDYEAR
#ARTIST --> attribution in OBJECTS database
#REGIONOFORIGIN --> 

db_path = snakemake.input[0]
con = duckdb.connect(db_path)

df = con.execute("""
    SELECT 
            attribution AS artist,
            beginyear AS birthyear,
            displaydate AS date,
        FROM objects  
        GROUP BY attribution, beginyear, displaydate
        ORDER BY beginyear DESC
                 """).df()

def format_year(year):
    if year is None:
        return "Unknown"
    year = int(year)
    if year <0:
        return f"{abs(year)} BC"
    else:
        return f"{year} AD"
    
df['birthyear'] = df['birthyear'].apply(format_year)
df.columns = ['Artist','Year','date']
df.index = df.index + 1

time = con.execute("""
SELECT
COUNT(CASE WHEN beginyear < 1000 THEN 1 END) AS before_1000,
COUNT(CASE WHEN beginyear >= 1000 AND beginyear < 1800 THEN 1 END) AS medieval_early_modern,
COUNT(CASE WHEN beginyear >= 1800 AND beginyear < 1900 THEN 1 END) AS nineteenth_century,
COUNT(CASE WHEN beginyear >= 1900 THEN 1 END) AS twentieth_century_on,
COUNT(CASE WHEN beginyear IS NULL THEN 1 END) AS unknown_year
FROM objects
""").df()

before_1000 = int(time['before_1000'][0])
medieval = int(time['medieval_early_modern'][0])
nineteenth = int(time['nineteenth_century'][0])
twentieth = int(time['twentieth_century_on'][0])
unknown = int(time['unknown_year'][0])
total = before_1000 + medieval + nineteenth + twentieth + unknown

labels = ['Before 1000 AD', 'Medieval & Early Modern\n(1000–1799)', '19th Century\n(1800–1899)', '20th Century+\n(1900–present)', 'Unknown']
sizes = [before_1000, medieval, nineteenth, twentieth, unknown]
colors = ['#3266ad', '#5a9e6f', '#c0925a', '#73726c', '#b0b0b0']
pcts = [f"{v/total*100:.1f}%" for v in sizes]

fig, ax = plt.subplots(figsize=(8, 6))
wedges, _ = ax.pie(
sizes,
colors=colors,
startangle=90,
wedgeprops=dict(width=0.55, edgecolor='white', linewidth=2)
)
ax.text(0, 0.08, f"{total:,}", ha='center', va='center',
fontsize=18, fontweight='bold', color='#2c2c2a')
ax.text(0, -0.18, "total objects", ha='center', va='center',
fontsize=10, color='#888780')

legend_labels = [f"{l}—{c:,}({p})" for l, c, p in zip(labels, sizes, pcts)]
patches = [mpatches.Patch(color=c, label=l) for c, l in zip(colors, legend_labels)]
ax.legend(handles=patches, loc='lower center', bbox_to_anchor=(0.5, -0.32),
frameon=False, fontsize=9, handlelength=1.2, handleheight=1.2)

ax.set_title("Museum objects by era", fontsize=14, fontweight='bold',
pad=16, color='#2c2c2a')

plt.tight_layout()
plt.savefig('results/Pieces_By_Timeperiod.png')
plt.close()

most_common = con.execute("""
    WITH categorized AS (
        SELECT
            attribution,
            CASE
                WHEN beginyear < 1000                        THEN 'Before 1000 AD'
                WHEN beginyear >= 1000 AND beginyear < 1800  THEN 'Medieval & Early Modern'
                WHEN beginyear >= 1800 AND beginyear < 1900  THEN '19th Century'
                WHEN beginyear >= 1900                       THEN '20th Century+'
            END AS era
        FROM objects
        WHERE attribution IS NOT NULL AND attribution != ''
        AND beginyear IS NOT NULL
    ),
    counts AS (
        SELECT era, attribution, COUNT(*) AS cnt
        FROM categorized
        GROUP BY era, attribution
    ),
    ranked AS (
        SELECT *,
               ROW_NUMBER() OVER (PARTITION BY era ORDER BY cnt DESC) AS rank
        FROM counts
    )
    SELECT era, attribution, cnt
    FROM ranked
    WHERE rank = 1
    ORDER BY CASE era
        WHEN 'Before 1000 AD'          THEN 1
        WHEN 'Medieval & Early Modern' THEN 2
        WHEN '19th Century'            THEN 3
        WHEN '20th Century+'           THEN 4
    END
""").df()

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

colors   = ['#E63946', '#F4A261', '#2A9D8F', '#6A0572']
era_order = ['Before 1000 AD', 'Medieval & Early Modern', '19th Century', '20th Century+']

for i, era in enumerate(era_order):
    row = most_common[most_common['era'] == era]
    if row.empty:
        artist = 'No data'
        cnt = 0
    else:
        artist = row['attribution'].values[0]
        cnt    = int(row['cnt'].values[0])

    x = i / len(era_order)
    w = 1 / len(era_order)

    ax.add_patch(plt.Rectangle((x + 0.02, 0.2), w - 0.04, 0.6,
                                color=colors[i], transform=ax.transAxes,
                                clip_on=False, zorder=2, linewidth=0,
                                joinstyle='round'))

    ax.text(x + w/2, 0.68, era, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white',
            transform=ax.transAxes, zorder=3)

    ax.text(x + w/2, 0.47, artist, ha='center', va='center',
            fontsize=9, color='white', transform=ax.transAxes,
            zorder=3)

    ax.text(x + w/2, 0.28, f"{cnt:,} people", ha='center', va='center',
        fontsize=8, color='white', alpha=0.85,
        transform=ax.transAxes, zorder=3)

ax.set_title("Which artist appeared the most often per era?", fontsize=14,
             fontweight='bold', color='#2c2c2a', pad=20)

plt.tight_layout()
plt.savefig('results/Most_Common_Artist_By_Era.png')
plt.close()

