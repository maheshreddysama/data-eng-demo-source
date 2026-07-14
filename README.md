## **Data Engineering Pipeline: GCS Ingestion & Dimensional Modeling**

A production-ready data engineering pipeline that ingests heterogeneous raw data sources (CSV, JSON, and Pipe-Delimited TXT) into an immutable Google Cloud Storage (GCS) Data Lakehouse landing zone (Bronze Layer) using Hive-style partitioning, preparing it for downstream dimensional modeling into a Star Schema.

## **🏗️ Architecture Overview**

1. **Data Source Layer (Local/Extracted):** - `customers.csv`: Structured relational metadata.
   - `products.json`: Semi-structured document records.
   - `orders_flat.txt`: High-throughput transaction records using pipe-delimiters (`|`).
2. **Ingestion Layer (Python SDK):** Robust ingestion script utilizing the Google Cloud Storage Python client library with explicit service account authentication and error logging.
3. **Storage Layer (GCS Raw Landing Zone):** Organizes incoming datasets dynamically using automated idempotent runtime execution folders structured as: `gs://<bucket_name>/<dataset>/dt=YYYY-MM-DD/file`.
4. **Analytical Layer (Dimensional Model Target):** Decomposes flat transaction files and normalized dimension tables into a robust analytical **Star Schema** utilizing deterministic hashing (`MD5`/`SHA-2`) for resilient, idempotent surrogate key generation.

## ** 📂 Project Structure**

data-eng-demo-source/
│
├── extracted/                  # Local landing directory for raw source data
│   ├── customers.csv           # Comma-separated customer profile records
│   ├── products.json           # Semi-structured JSON array of product catalog data
│   └── orders_flat.txt         # Pipe-delimited transactional sales stream
│
├── load_to_gcs.py              # Main Python ETL pipeline orchestrating GCS uploads
├── README.md                   # Project documentation and deployment blueprint
└── key.json                    # Google Service Account IAM Credentials (⚠️ GIT IGNORED)

## 🛠️ Step-by-Step Implementation Guide

### Phase 1: Google Cloud Platform Setup

1. **Create Project & Bind Billing:** - Create a project named `DE Demo`. Link an active billing account via the GCP Console to unlock the Storage API backend.
2. **Enable Cloud Storage API:**
* Navigate to **APIs & Services > Library**, search for **Google Cloud Storage JSON API**, and click **Enable**.


3. **Configure Organization Policy (For Standalone/Personal Accounts):**
* Navigate to **Organization Policies** at the project level.
* Search for `iam.disableServiceAccountKeyCreation` (*Disable service account key creation*).
* Click **Manage Policy**, choose **Customize**, add a rule, set **Enforcement to Off**, and Save.


4. **Create GCS Landing Zone Bucket:**
* Create a globally unique bucket named `de-demo-raw-zone` in your preferred regional proximity (e.g., `northamerica-northeast2` / Toronto).


5. **Provision Service Account Credentials:**
* Go to **IAM & Admin > Service Accounts** and create `de-pipeline-sa`.
* Grant the service account the **Storage Object Admin** role.
* Navigate to the **Keys** tab, click **Add Key > Create New Key > JSON**.
* Save the downloaded file into your local project workspace as `key.json`.

### Phase 2: Local Environment Setup

Ensure you are running Python 3.11+. Install the required cloud storage client binaries inside your active terminal environment:

```bash
# Using PowerShell or Command Prompt
python -m pip install google-cloud-storage

```

---

### Phase 3: Run Ingestion Pipeline

1. Populate the `extracted/` folder with your test datasets.
2. Ensure your `load_to_gcs.py` file points to your precise **Project ID** and local `key.json` pathway.
3. Execute the pipeline:

```bash
python load_to_gcs.py

```

**Expected Log Output:**

```text
Uploaded to gs://de-demo-raw-zone/customers/dt=2026-07-13/customers.csv
Uploaded to gs://de-demo-raw-zone/products/dt=2026-07-13/products.json
Uploaded to gs://de-demo-raw-zone/orders/dt=2026-07-13/orders_flat.txt

```

---

## 📊 Downstream Data Warehouse Modeling (Star Schema)

Once data lands safely inside the GCS storage layer, it is prepared for ingestion into a cloud data warehouse (Snowflake, Databricks, or Microsoft Fabric) using the following data model mappings:

### 1. Dimension Tables (The Context)

* **`DimCustomer`**: Built by extracting `distinct` entries from `customers.csv`.
* `CustomerKey` (Surrogate Key via `MD5(customer_id)`)
* `customer_id` (Natural Key), `name`, `email`, `signup_date`, `country`


* **`DimProduct`**: Built from flattening and parsing `products.json`.
* `ProductKey` (Surrogate Key via `MD5(product_id)`)
* `product_id` (Natural Key), `name`, `category`, `price`, `supplier`



### 2. Fact Table (The Metrics)

* **`FactSales`**: Parsed directly from the flat transaction tracking file `orders_flat.txt`, mapping to surrogate keys via inner joins over natural keys to ensure spatial optimization and analytical performance.
* `TransactionID` / `OrderID`
* `CustomerKey` (Foreign Key pointing to `DimCustomer`)
* `ProductKey` (Foreign Key pointing to `DimProduct`)
* `OrderDate`, `Quantity`, `TotalAmount`



---

## 🔒 Security Practices

* **Never commit credential keys:** Ensure `key.json` is explicitly appended to your `.gitignore` profile before tracking project revisions via GitHub.
* **Least-Privilege Principle:** The pipeline service account utilizes dedicated `Storage Object Admin` context, limiting vulnerability exposure scope strictly to the data lake container bounds.
"""

# Write the contents out to a physical file

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content.strip())

print("README.md generated successfully.")

```
Your Markdown file is ready
[file-tag: code-generated-file-0-1783989798386048190]

I have generated a clean, comprehensive, and professional **`README.md`** file tailored perfectly to your project directory, files, and architecture. It describes your layout, configuration fixes (like the organization policy for service account keys), execution steps, and the final Star Schema modeling strategy.

You can copy and paste the markdown text below straight into your local workspace file:

```markdown
# Data Engineering Pipeline: GCS Ingestion & Dimensional Modeling

A production-ready data engineering pipeline that ingests heterogeneous raw data sources (CSV, JSON, and Pipe-Delimited TXT) into an immutable Google Cloud Storage (GCS) Data Lakehouse landing zone (Bronze Layer) using Hive-style partitioning, preparing it for downstream dimensional modeling into a Star Schema.

## 🏗️ Architecture Overview

1. **Data Source Layer (Local/Extracted):**
   - `customers.csv`: Structured relational metadata.
   - `products.json`: Semi-structured document records.
   - `orders_flat.txt`: High-throughput transaction records using pipe-delimiters (`|`).
2. **Ingestion Layer (Python SDK):** Robust ingestion script utilizing the Google Cloud Storage Python client library with explicit service account authentication and error logging.
3. **Storage Layer (GCS Raw Landing Zone):** Organizes incoming datasets dynamically using automated idempotent runtime execution folders structured as: `gs://<bucket_name>/<dataset>/dt=YYYY-MM-DD/file`.
4. **Analytical Layer (Dimensional Model Target):** Decomposes flat transaction files and normalized dimension tables into a robust analytical **Star Schema** utilizing deterministic hashing (`MD5`/`SHA-2`) for resilient, idempotent surrogate key generation.

---

## 📂 Project Structure

```text
data-eng-demo-source/
│
├── extracted/                  # Local landing directory for raw source data
│   ├── customers.csv           # Comma-separated customer profile records
│   ├── products.json           # Semi-structured JSON array of product catalog data
│   └── orders_flat.txt         # Pipe-delimited transactional sales stream
│
├── load_to_gcs.py              # Main Python ETL pipeline orchestrating GCS uploads
├── README.md                   # Project documentation and deployment blueprint
└── key.json                    # Google Service Account IAM Credentials (⚠️ GIT IGNORED)

```

---

## 🛠️ Step-by-Step Implementation Guide

### Phase 1: Google Cloud Platform Setup

1. **Create Project & Bind Billing:**
* Create a project named `DE Demo`. Link an active billing account via the GCP Console to unlock the Storage API backend.


2. **Enable Cloud Storage API:**
* Navigate to **APIs & Services > Library**, search for **Google Cloud Storage JSON API**, and click **Enable**.


3. **Configure Organization Policy (For Standalone/Personal Accounts):**
* Navigate to **Organization Policies** at the project level.
* Search for `iam.disableServiceAccountKeyCreation` (*Disable service account key creation*).
* Click **Manage Policy**, choose **Customize**, add a rule, set **Enforcement to Off**, and Save.


4. **Create GCS Landing Zone Bucket:**
* Create a globally unique bucket named `de-demo-raw-zone` in your preferred regional proximity (e.g., `northamerica-northeast2` / Toronto).


5. **Provision Service Account Credentials:**
* Go to **IAM & Admin > Service Accounts** and create `de-pipeline-sa`.
* Grant the service account the **Storage Object Admin** role.
* Navigate to the **Keys** tab, click **Add Key > Create New Key > JSON**.
* Save the downloaded file into your local project workspace as `key.json`.



---

### Phase 2: Local Environment Setup

Ensure you are running Python 3.11+. Install the required cloud storage client binaries inside your active terminal environment:

```bash
# Using PowerShell or Command Prompt
python -m pip install google-cloud-storage

```

---

### Phase 3: Run Ingestion Pipeline

1. Populate the `extracted/` folder with your test datasets.
2. Ensure your `load_to_gcs.py` file points to your precise **Project ID** and local `key.json` pathway.
3. Execute the pipeline:

```bash
python load_to_gcs.py

```

**Expected Log Output:**

```text
Uploaded to gs://de-demo-raw-zone/customers/dt=2026-07-13/customers.csv
Uploaded to gs://de-demo-raw-zone/products/dt=2026-07-13/products.json
Uploaded to gs://de-demo-raw-zone/orders/dt=2026-07-13/orders_flat.txt

```

---

## 📊 Downstream Data Warehouse Modeling (Star Schema)

Once data lands safely inside the GCS storage layer, it is prepared for ingestion into a cloud data warehouse (Snowflake, Databricks, or Microsoft Fabric) using the following data model mappings:

### 1. Dimension Tables (The Context)

* **`DimCustomer`**: Built by extracting `distinct` entries from `customers.csv`.
* `CustomerKey` (Surrogate Key via `MD5(customer_id)`)
* `customer_id` (Natural Key), `name`, `email`, `signup_date`, `country`


* **`DimProduct`**: Built from flattening and parsing `products.json`.
* `ProductKey` (Surrogate Key via `MD5(product_id)`)
* `product_id` (Natural Key), `name`, `category`, `price`, `supplier`



### 2. Fact Table (The Metrics)

* **`FactSales`**: Parsed directly from the flat transaction tracking file `orders_flat.txt`, mapping to surrogate keys via inner joins over natural keys to ensure spatial optimization and analytical performance.
* `TransactionID` / `OrderID`
* `CustomerKey` (Foreign Key pointing to `DimCustomer`)
* `ProductKey` (Foreign Key pointing to `DimProduct`)
* `OrderDate`, `Quantity`, `TotalAmount`



---

## 🔒 Security Practices

* **Never commit credential keys:** Ensure `key.json` is explicitly appended to your `.gitignore` profile before tracking project revisions via GitHub.
* **Least-Privilege Principle:** The pipeline service account utilizes dedicated `Storage Object Admin` context, limiting vulnerability exposure scope strictly to the data lake container bounds.

```

```
