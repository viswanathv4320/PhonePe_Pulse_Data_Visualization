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
PhonePe_Pulse_Data_Visualization/
│
├── app.py
├── data_extraction.py # Read raw JSON → Python dicts/lists
├── data_transform.py # Clean & normalize → Pandas DataFrames
├── db_handler.py # Create MySQL tables
├── db_inserter.py # Bulk insert helpers for ETL
├── load_data.py # Orchestrates extract → transform → load
├── 2011_Dist.geojson
├── india_state_geo.json
├── pulse/ # PhonePe Pulse dataset (to extract data)
├── requirements.txt # Python deps
├── .gitignore # Ignore rules
└── README.md


---

## 📦 Installation

### 1) Clone the repo

If you’re using **submodules** for the dataset:

git clone https://github.com/viswanathv4320/PhonePe_Pulse_Data_Visualization.git
cd PhonePe_Pulse_Data_Visualization
git submodule update --init --recursive

### 2) Create a virtual environment & install deps

python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

---

## Tech Stack

Python 3.12, Pandas, Plotly
Streamlit (UI)
MySQL (optional ETL)
GeoJSON layers for state/district boundaries



