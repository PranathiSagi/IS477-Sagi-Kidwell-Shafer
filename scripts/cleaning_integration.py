import pandas as pd
import duckdb
import os
import snakemake

#read CSVs from the National Gallery of Art's opendata repository
constituents_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/08bc72ca5fccf86ca4f3702f9db068a11a592509/data/constituents.csv'
cons_df = pd.read_csv(constituents_url)
objects_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/refs/heads/main/data/objects.csv'
objects_df = pd.read_csv(objects_url)
objects_constituents_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/refs/heads/main/data/objects_constituents.csv'
objects_cons_df = pd.read_csv(objects_constituents_url)
text_entries_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/refs/heads/main/data/objects_text_entries.csv'
text_entries_df = pd.read_csv(text_entries_url)
media_items_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/refs/heads/main/data/media_items.csv'
media_df = pd.read_csv(media_items_url)
media_relationships_url = 'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/refs/heads/main/data/media_relationships.csv'
media_relationships_df = pd.read_csv(media_relationships_url)

#data cleaning
limit = len(objects_df) * 0.7
objects_df = objects_df.dropna(thresh=limit, axis=1)

target_cols = ['medium', 'dimensions', 'inscription', 'markings', 'provenancetext']
available_cols = [col for col in target_cols if col in objects_df.columns]
objects_df[available_cols] = objects_df[available_cols].fillna("Unknown")

objects_df = objects_df.dropna(subset=['beginyear', 'endyear', 'creditline', 'visualbrowsertimespan'])

if 'displaydate' in objects_df.columns:
    objects_df['displaydate'] = objects_df['displaydate'].fillna(objects_df['beginyear'].astype(str))   
if 'wikidataid' in objects_df.columns:
    objects_df['wikidataid'] = objects_df['wikidataid'].fillna('Not Linked')

objects_cons_df['objectid'] = objects_cons_df['objectid'].replace(0, 'NaN')

remove = ['anonymous artist', 'anonymous']
cons_df['preferreddisplayname'] = cons_df['preferreddisplayname'].str.lower().str.strip()
cons_df['preferreddisplayname'] = cons_df['preferreddisplayname'].replace(remove, 'Anonymous')
cons_df['forwarddisplayname'] = cons_df['forwarddisplayname'].str.lower().str.strip()
cons_df['forwarddisplayname'] = cons_df['forwarddisplayname'].replace(remove, 'Anonymous')

#creating duckdb database
con = duckdb.connect("Museum.db")

con.sql("DROP TABLE IF EXISTS media_relationships")
con.sql("DROP TABLE IF EXISTS text_entries")
con.sql("DROP TABLE IF EXISTS objects_cons")
con.sql("DROP TABLE IF EXISTS objects")
con.sql("DROP TABLE IF EXISTS cons")
con.sql("DROP TABLE IF EXISTS media")

con.sql("""
CREATE OR REPLACE TABLE objects AS
SELECT * FROM objects_df
""")

con.sql("""
CREATE OR REPLACE TABLE cons AS
SELECT * FROM cons_df
""")

con.sql("""
CREATE OR REPLACE TABLE media AS
SELECT * FROM media_df
""")

con.sql("""
CREATE OR REPLACE TABLE media_relationships AS
SELECT * FROM media_relationships_df
""")

con.sql("""
CREATE OR REPLACE TABLE text_entries AS
SELECT * FROM text_entries_df
""")

con.sql("""
CREATE OR REPLACE TABLE objects_cons AS
SELECT * FROM objects_df
""")

#outputting SQL file
sql_script = """
CREATE OR REPLACE TABLE objects AS
SELECT * FROM objects_df;

CREATE OR REPLACE TABLE cons AS
SELECT * FROM cons_df;

CREATE OR REPLACE TABLE media AS
SELECT * FROM media_df;

CREATE OR REPLACE TABLE media_relationships AS
SELECT * FROM media_relationships_df;

CREATE OR REPLACE TABLE text_entries AS
SELECT * FROM text_entries_df;

CREATE OR REPLACE TABLE objects_cons AS
SELECT * FROM objects_df;
"""

with open("museum_database_export.sql", "w") as f:
    f.write(sql_script)

#exporting database
# con.sql("""
# EXPORT DATABASE 'Museum'
# """)