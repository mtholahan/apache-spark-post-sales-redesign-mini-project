# Spark Mini Project: Automobile Post-Sales Accident Report

This project uses Apache Spark to analyze a dataset of vehicle incident history and outputs a report of total accident counts per vehicle make and year.

## 📂 Project Structure

- `autoinc_spark.py` – Main Spark job script
- `run.sh` – Shell script to execute the Spark job
- `data.csv` – Input dataset (must be present in the same directory)
- `output/` – Output directory containing accident counts
- `Execution-Log.txt` – Captured terminal output from a successful run

## ▶️ How to Run

### Prerequisites
- Python 3.x
- PySpark installed
- Virtual environment (optional but recommended)
- Spark properly configured (local mode is fine)

### Step-by-Step

1. Open terminal and navigate to this project folder:
   ```bash
   cd ~/spark_projects/post_sales_report
   ```

2. Make the shell script executable (only needed once):
   ```bash
   chmod +x run.sh
   ```

3. Run the project:
   ```bash
   ./run.sh
   ```

4. View the output:
   ```bash
   cat output/part-00000
   ```

You should see output similar to:
```
Nissan-2003,1
Mercedes-2015,2
Mercedes-2016,1
```

## 📋 Notes
- If output already exists, it will be automatically removed before each run.
- Any accident record without a matching VIN from an initial sale (`I`) will be ignored.
- This script processes a non-headered CSV file.

## 🧪 Verification
See `Execution-Log.txt` for a full trace of a successful Spark job run.

---

Feel free to fork and extend. Enjoy Spark!