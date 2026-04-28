rule run_all:
        input:
            "Museum.db",
            "museum_database_export.sql",
            "results/Play_URL_Status_Codes.png",
            "results/Thumbnail_URL_Status_Codes.png",
            "results/Download_URL_Status_Codes.png",
            "results/Image_URL_Status_Codes.png",
            "results/Traditional_vs_Digital_Object_Distribution.png"

rule prepare_data:
        output:
            "Museum.db",
            "museum_database_export.sql"
        shell:
            "python scripts/cleaning_integration.py"

rule researchQ1:
        input:
            "Museum.db"
        output:
            "results/Play_URL_Status_Codes.png",
            "results/Thumbnail_URL_Status_Codes.png",
            "results/Download_URL_Status_Codes.png",
            "results/Image_URL_Status_Codes.png"
        shell:
            "python scripts/researchQ1.py"

rule researchQ2:
        input:
            "Museum.db"
        output:
            "results/Traditional_vs_Digital_Object_Distribution.png"
        shell:
            "python scripts/researchQ2.py"