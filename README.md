# 📊 PhonePe Pulse Data Visualization Dashboard

An interactive **Streamlit** dashboard for exploring the **PhonePe Pulse** dataset, with **Plotly visualizations** and optional MySQL database integration for ETL and analytics.

This project extracts, cleans, and visualizes PhonePe Pulse data across **transactions**, **users**, and **insurance** metrics at both state and district levels.

---

## 🚀 Features
- **Interactive visualizations** using Plotly and Streamlit
- **Geo-visualization** at state and district level
- **ETL pipeline** to store data into MySQL
- **Data cleaning & transformation** for consistent formats
- **Support for PhonePe Pulse dataset as a Git submodule** (or fetch script)
- Analysis by:
  - Top states/districts by transaction volume and amount
  - User metrics (registrations, app opens, brand distribution)
  - Insurance premiums and counts

---

## 📂 Project Structure
```
PhonePe_Pulse_Data_Visualization/
│
├── app.py                          # Streamlit UI
├── data_extraction.py              # Read raw JSON → Python dicts/lists
├── data_transform.py               # Clean & normalize → Pandas DataFrames
├── db_handler.py                   # Create MySQL tables
├── db_inserter.py                  # Bulk insert helpers for ETL
├── load_data.py                    # Orchestrates extract → transform → load
├── 2011_Dist.geojson               # District boundaries
├── india_state_geo.json            # State boundaries
├── pulse/                          # PhonePe Pulse dataset (submodule or local)
├── requirements.txt                # Python deps
├── .gitignore                      # Ignore rules
└── README.md
```

---

## 📦 Installation

### 1) Clone the repo

**If you’re using `pulse/` as a submodule (recommended):**
```bash
git clone https://github.com/viswanathv4320/PhonePe_Pulse_Data_Visualization.git
cd PhonePe_Pulse_Data_Visualization
git submodule update --init --recursive
```

**If you prefer to fetch the dataset without submodules (keep repo small):**
```bash
git clone https://github.com/viswanathv4320/PhonePe_Pulse_Data_Visualization.git
cd PhonePe_Pulse_Data_Visualization
python scripts/fetch_pulse_data.py   # see Dataset section below
```

---

### 2) Create a virtual environment & install deps
```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

---

## 🗂️ Dataset

You can obtain the official **PhonePe Pulse** dataset in two ways:

### Option A — Submodule
```bash
git submodule update --init --recursive
```

### Option B — Fetch script
`scripts/fetch_pulse_data.py`:
```python
import os, subprocess

URL = "https://github.com/PhonePe/pulse.git"
TARGET = "pulse"

if not os.path.exists(TARGET):
    subprocess.check_call(["git", "clone", "--depth", "1", URL, TARGET])
else:
    subprocess.check_call(["git", "-C", TARGET, "pull", "--ff-only"])
print("Pulse dataset ready at ./pulse")
```
Run it:
```bash
python scripts/fetch_pulse_data.py
```

---

## ▶️ Run the Dashboard
```bash
streamlit run app.py
```
Open the URL printed in your terminal (usually http://localhost:8501).

---

## ⚙️ Optional: MySQL ETL

1) Create the database:
```sql
CREATE DATABASE phonepe_pulse;
```

2) Update credentials in `db_handler.py` / `db_inserter.py`:
```python
host = "localhost"
user = "root"
password = "your_password"
database = "phonepe_pulse"
```

3) Create tables:
```bash
python db_handler.py
```

4) Load data:
```bash
python load_data.py
```

---

## ✅ Requirements
From `requirements.txt`:
```text
streamlit
pandas
numpy
plotly
mysql-connector-python
```

---

## 🧹 .gitignore
```gitignore
# OS
.DS_Store

# Python
__pycache__/
*.py[cod]

# Virtual envs
.venv/
venv/

# Secrets / local config
.env
my.cnf

# Big binaries not needed for code review
*.pdf
*.zip

# Optional: ignore dataset if not using submodule
# pulse/
```

---

## 🔍 Troubleshooting

- **`pulse` shows as a pointer on GitHub**  
  Initialize submodule:
  ```bash
  git submodule update --init --recursive
  ```

- **Dataset not found**  
  Ensure `./pulse` exists and contains `data/aggregated`, `data/map`, and `data/top`.

- **MySQL errors**  
  Verify service is running and credentials are correct:
  ```bash
  mysql -u root -p -e "SHOW DATABASES;"
  ```

---

## 🛠️ Tech Stack
- Python 3.12
- Streamlit (UI)
- Plotly (visualizations)
- Pandas (data manipulation)
- MySQL (optional ETL)
- GeoJSON layers for state/district boundaries

---

## 📜 License
This project is for **educational and personal use**.  
PhonePe Pulse data is owned by **PhonePe** under their terms.

---

## 👤 Author
**Viswanath Vadlamani**  
GitHub: [@viswanathv4320](https://github.com/viswanathv4320)  
Email: *add your email here*

---

## 🙌 Contributing
1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "feat: add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request
