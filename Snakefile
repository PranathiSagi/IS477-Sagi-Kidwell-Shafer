rule run_all:
        input:
            "Museum.db",
            "museum_database_export.sql",
            "results/Play_URL_Status_Codes.png",
            "results/Thumbnail_URL_Status_Codes.png",
            "results/Download_URL_Status_Codes.png",
            "results/Image_URL_Status_Codes.png",
            "results/Traditional_vs_Digital_Object_Distribution.png",
            "results/Pieces_By_Timeperiod.png",
            "results/Most_Common_Artist_By_Era.png"

rule researchQ1:
        input:
            "Museum.db"
        output:
            "results/Play_URL_Status_Codes.png",
            "results/Thumbnail_URL_Status_Codes.png",
            "results/Download_URL_Status_Codes.png",
            "results/Image_URL_Status_Codes.png"
        script:
            "scripts/researchQ1.py"

rule researchQ2:
        input:
            "Museum.db"
        output:
            "results/Traditional_vs_Digital_Object_Distribution.png"
        script:
            "scripts/researchQ2.py"

rule researchQ3:
        input:
            "Museum.db"
        output:
            "results/Pieces_By_Timeperiod.png",
            "results/Most_Common_Artist_By_Era.png"
        script:
            "scripts/researchQ3.py"