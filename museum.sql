
    
     CREATE OR REPLACE TABLE objects (
        PRIMARY KEY (objectid),
        objectid INTEGER,
        uuid TEXT,
        accessioned INTEGER,
        accessionnum TEXT,
        title TEXT,
        displaydate DATE,
        beginyear FLOAT,
        endyear FLOAT,
        visualbrowsertimespan TEXT,
        medium TEXT,
        dimensions TEXT,
        attributioninverted TEXT,
        attribution TEXT,
        creditline TEXT,
        isvirtual INTEGER,
        departmntabbr TEXT,
        lastdetectmodification TEXT,
        wikidataid TEXT,
        merged_classification TEXT,
        );
               
    CREATE OR REPLACE TABLE cons (
        constituentid INTEGER,
        uuid object,
        ulanid FLOAT,
        preferreddisplayname TEXT,
        forwarddisplayname TEXT,
        lastname TEXT,
        displaydate TEXT,
        artistofngaobject INT,
        beginyear FLOAT,
        endyear FLOAT,
        visualbrowsertimespan TEXT,
        nationality TEXT,
        visualbrowsernationality TEXT,
        constituenttype TEXT,
        wikidataid TEXT,
        PRIMARY KEY (constituentid INT),
    );
    
    CREATE OR REPLACE TABLE media (
        mediaid	INTEGER,
        mediatype TEXT,
        title TEXT,
        description TEXT,
        duration FLOAT,
        language TEXT,
        thumbnailurl TEXT,
        playurl TEXT,
        downloadurl TEXT,
        keywords TEXT,
        tags TEXT,
        imageurl TEXT,
        presentationdate DATE,
        releasedate DATE,
        lastmodified DATE,
        PRIMARY KEY (mediaid)
    );
    
    CREATE OR REPLACE TABLE media_relationships (
        mediaid INTEGER,
        relatedid INTEGER,
        relatedentity TEXT,
        PRIMARY KEY (mediaid, relatedid),
        FOREIGN KEY (mediaid) REFERENCES media(mediaid),
        FOREIGN KEY (relatedid) REFERENCES objects(objectid)
    );
               
    CREATE OR REPLACE TABLE text_entries (
        objectid INTEGER,
        text TEXT,
        texttype TEXT,
        year FLOAT,
        FOREIGN KEY (objectid) REFERENCES objects(objectid),
    );
    
    CREATE OR REPLACE TABLE objects_cons (
        objectid INTEGER,
        constituentid INTEGER,
        displayorder INTEGER,
        roletype TEXT,
        role TEXT,
        prefix TEXT,
        suffix TEXT,
        displaydate TEXT,
        beginyear FLOAT,
        endyear FLOAT,
        country TEXT,
        zipcode TEXT,
        PRIMARY KEY (objectid),
        FOREIGN KEY (constituentid) REFERENCES cons(constituentid),
    );
    
    