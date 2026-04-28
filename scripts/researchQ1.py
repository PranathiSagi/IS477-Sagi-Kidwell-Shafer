import duckdb
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

db_path = snakemake.input[0]
con = duckdb.connect(db_path)

digital_objects = con.sql("SELECT * FROM media").df()
def visit_website(url):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code
    except Exception:
        return "Error"

with ThreadPoolExecutor(max_workers=20) as executor:
    digital_objects['play_url_status_code'] = list(executor.map(visit_website, digital_objects['playurl']))

with ThreadPoolExecutor(max_workers=20) as executor:
    digital_objects['thumbnailurl_status_code'] = list(executor.map(visit_website, digital_objects['thumbnailurl']))

with ThreadPoolExecutor(max_workers=20) as executor:
    digital_objects['downloadurl_status_code'] = list(executor.map(visit_website, digital_objects['downloadurl']))

with ThreadPoolExecutor(max_workers=20) as executor:
    digital_objects['imageurl_status_code'] = list(executor.map(visit_website, digital_objects['imageurl']))

play_counts = pd.DataFrame(digital_objects.play_url_status_code.value_counts())
thumbnail_counts = pd.DataFrame(digital_objects.thumbnailurl_status_code.value_counts())
download_counts = pd.DataFrame(digital_objects.downloadurl_status_code.value_counts())
image_counts = pd.DataFrame(digital_objects.imageurl_status_code.value_counts())
plt.pie(play_counts["count"], labels=play_counts.index, autopct='%1.1f%%')
plt.title("Play URL Status Codes")
plt.savefig('results/Play_URL_Status_Codes.png')

plt.pie(thumbnail_counts["count"], labels=thumbnail_counts.index, autopct='%1.1f%%')
plt.title("Thumbnail URL Status Codes")
plt.savefig('results/Thumbnail_URL_Status_Codes.png')

plt.pie(download_counts["count"], labels=download_counts.index, autopct='%1.1f%%')
plt.title("Download URL Status Codes")
plt.savefig('results/Download_URL_Status_Codes.png')

plt.pie(image_counts["count"], labels=image_counts.index, autopct='%1.1f%%')
plt.title("Image URL Status Codes")
plt.savefig('results/Image_URL_Status_Codes.png')