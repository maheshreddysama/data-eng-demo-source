# load_to_gcs.py
from google.cloud import storage
import os
from datetime import date
from google.cloud import storage
import os
from datetime import date

# Tell Python where your service account key is located
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\mahes\Downloads\key.json.json" 
PROJECT_ID = "de-demo-502320"
BUCKET = "de-demo-raw-zone"

today = date.today().isoformat()

def upload(local_path, gcs_folder):
    client = storage.Client()
    bucket = client.bucket(BUCKET)
    filename = os.path.basename(local_path)
    blob_path = f"{gcs_folder}/dt={today}/{filename}"
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded to gs://{BUCKET}/{blob_path}")

if __name__ == "__main__":
    upload("extracted/customers.csv", "customers")
    upload("extracted/products.json", "products")
    upload("extracted/orders_flat.txt", "orders")