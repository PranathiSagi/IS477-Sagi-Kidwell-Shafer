COPY cons FROM 'museum_db_export/cons.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
COPY media FROM 'museum_db_export/media.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
COPY media_relationships FROM 'museum_db_export/media_relationships.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
COPY objects FROM 'museum_db_export/objects.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
COPY objects_cons FROM 'museum_db_export/objects_cons.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
COPY text_entries FROM 'museum_db_export/text_entries.csv' (FORMAT 'csv', quote '"', delimiter ',', header 1);
