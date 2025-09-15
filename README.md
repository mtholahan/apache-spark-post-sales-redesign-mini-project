# Apache Spark Post Sales Redesign Mini Project


## 📖 Abstract
This project focuses on performance tuning of PySpark jobs, transforming inefficient queries into optimized Spark workloads. The exercise highlights how Spark’s performance can degrade when queries are poorly structured, with excessive shuffles, suboptimal operators, or imbalanced partitioning.

The provided baseline code (optimize.py) attempted to compute the number of answers per question per month but did so inefficiently, generating unnecessary shuffles and intermediate results. My task was to analyze the physical execution plan and apply best practices in Spark optimization.

Key improvements included:

* Operator choice: replacing costly transformations with more efficient APIs.

* Shuffle minimization: reducing data movement through judicious use of groupBy, join, and mapPartitions.

* Partition tuning: rebalancing data distribution to avoid stragglers.

* Data format selection: leveraging columnar storage for downstream efficiency.

Through this project, I gained practical experience in reading Spark's execution plans, identifying bottlenecks, and applying a structured approach to performance tuning. The optimized pipeline produced the same results as the baseline but with significantly reduced runtime, demonstrating how developer choices directly impact big data job performance.



## 🛠 Requirements
- Apache Spark 3.x (local or cluster mode)
- Hadoop HDFS accessible (local Hortonworks sandbox recommended)
- Python 3.8+
- Input dataset: automobile incident history (data.csv)
- GitHub repo with Spark script (autoinc_spark.py), shell script, README, and logs



## 🧰 Setup
- Place input file data.csv into HDFS (or local FS for testing)
- Ensure Spark and Hadoop sandbox are running
- Clone repository
- Verify autoinc_spark.py and run_spark.sh are executable



## 📊 Dataset
- Automobile incident history dataset (data.csv)
- Columns: incident_id, incident_type (I/A/R), vin_number, make, model, year,
  incident_date, description



## ⏱️ Run Steps
- Submit Spark job with:
  spark-submit autoinc_spark.py
- Script flow:
  1. Load input data
  2. Propagate make/year info into accident records using VIN as key
  3. Filter accident incidents
  4. Map to (make-year, 1) key-value pairs
  5. Aggregate counts via reduceByKey
  6. Save output as CSV in HDFS



## 📈 Outputs
- CSV files written to HDFS with accident counts per make-year
- Example output:
  Nissan-2003,1
  BMW-2008,10
  MERCEDES-2013,2



## 📸 Evidence

![spark_job_log.png](./evidence/spark_job_log.png)  
Screenshot of successful Spark job execution

![hdfs_output.png](./evidence/hdfs_output.png)  
Screenshot of accident counts written to HDFS




## 📎 Deliverables

- [`- autoinc_spark.py (Spark job)`](./deliverables/- autoinc_spark.py (Spark job))

- [`- run_spark.sh (shell script wrapper)`](./deliverables/- run_spark.sh (shell script wrapper))

- [`- README with setup + run steps`](./deliverables/- README with setup + run steps)

- [`- Raw output files in /deliverables/ (CSV results from HDFS)`](./deliverables/- Raw output files in /deliverables/ (CSV results from HDFS))

- [`- Logs in /deliverables/ (command-line job output)`](./deliverables/- Logs in /deliverables/ (command-line job output))




## 🛠️ Architecture
- Spark job running on Hadoop sandbox
- RDD transformations (map, groupByKey, flatMap, reduceByKey)
- Input: CSV in HDFS
- Output: accident counts by make-year in HDFS CSVs



## 🔍 Monitoring
- Observe Spark job logs in console
- Inspect HDFS output folder for generated CSV files



## ♻️ Cleanup
- Remove HDFS output directory before re-running job
- Shut down Hadoop sandbox VM if not needed



*Generated automatically via Python + Jinja2 + SQL Server table `tblMiniProjectProgress` on 09-14-2025 23:49:19*