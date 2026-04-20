
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
