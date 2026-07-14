# extract.py
import requests, base64, os

REPO = "maheshreddysama/data-eng-demo-source"
BRANCH = "main"
FILES = ["customers.csv", "products.json", "orders_flat.txt"]
OUT_DIR = "extracted"

def fetch_file(path):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}?ref={BRANCH}"
    resp = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})
    resp.raise_for_status()
    content = base64.b64decode(resp.json()["content"])
    os.makedirs(OUT_DIR, exist_ok=True)
    local_path = os.path.join(OUT_DIR, path)
    with open(local_path, "wb") as f:
        f.write(content)
    return local_path

if __name__ == "__main__":
    for f in FILES:
        print(fetch_file(f))