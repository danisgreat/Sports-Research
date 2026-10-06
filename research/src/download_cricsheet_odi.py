import os
import urllib.request
import zipfile

DATA_DIR = os.path.join(os.getcwd(), "research", "data", "cricsheet_odi")
os.makedirs(DATA_DIR, exist_ok=True)
ZIP_PATH = os.path.join(DATA_DIR, "odis_male_json.zip")

url = "https://cricsheet.org/downloads/odis_male_json.zip"

print(f"Downloading {url} to {ZIP_PATH}...")
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response, open(ZIP_PATH, "wb") as out_file:
    data = response.read()
    out_file.write(data)

print(f"Downloaded {len(data) / (1024*1024):.2f} MB.")

EXTRACT_DIR = os.path.join(DATA_DIR, "matches")
os.makedirs(EXTRACT_DIR, exist_ok=True)
print(f"Extracting to {EXTRACT_DIR}...")
with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_DIR)

extracted_files = [f for f in os.listdir(EXTRACT_DIR) if f.endswith(".json")]
print(f"Successfully extracted {len(extracted_files)} ODI match JSON files!")
