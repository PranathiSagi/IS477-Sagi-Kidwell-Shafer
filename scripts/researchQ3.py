import duckdb
import pandas as pd
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