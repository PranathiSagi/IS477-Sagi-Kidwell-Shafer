import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import snakemake

db_path = snakemake.input.db
con = duckdb.connect(db_path)

result_df = con.sql("""
    SELECT 
        m.*, 
        mr.relatedid, 
        mr.relatedentity,
        o.*
    FROM media_df AS m
    FULL OUTER JOIN media_relationships_df AS mr 
    ON m.mediaid = mr.mediaid FULL OUTER JOIN 
    objects_df AS o ON mr.relatedid = o.objectid
""").df()

traditional_counts = result_df["mediaid"].isna().sum()
media_counts = len(result_df["mediaid"].dropna())
sns.barplot(x=['Traditional Objects', 'Digital Media'], y=[traditional_counts, media_counts])
plt.title("Distribution of Traditional Objects vs Digital Media")
plt.ylabel("Count")
plt.savefig('results/Traditional_vs_Digital_Object_Distribution.png')