# Apache Spark Post Sales Redesign Mini Project


## 📖 Abstract
This project focuses on redesigning an existing post-sales data pipeline in Apache Spark. You are tasked with generating a refreshed sales report using historical and customer churn data. The goal is to restructure the existing pipeline for improved maintainability, incorporate Spark SQL transformations, and deliver insights for business decision-makers. The redesigned pipeline outputs refined datasets and aggregated metrics useful for post-sales analysis.



## 🛠 Requirements
- Apache Spark (Databricks or local Spark environment)
- Customer churn and post-sales datasets (CSV format)
- Proficiency in PySpark and Spark SQL
- Ability to use Spark DataFrames and write clean transformation logic
- Optional: Data visualization tools or export to CSV



## 🧰 Setup
- Download the legacy post-sales datasets
- Inspect the provided starter Spark pipeline
- Create a new Spark notebook or script
- Redesign and implement data transformations
- Run job and validate output for accuracy



## 📊 Dataset
- Input: Historical post-sales and customer churn data in CSV format
- Fields include customer ID, churn flag, purchase history, plan type, and region
- Data loaded into Spark DataFrames for transformation and aggregation



## ⏱️ Run Steps
- Read datasets into Spark DataFrames
- Clean and transform raw fields using PySpark
- Apply business rules to derive metrics (e.g., churn rate, sales trends)
- Write final output to a CSV or display DataFrame
- Optionally visualize results or export to downstream systems



## 📈 Outputs
- Aggregated dataset summarizing post-sales trends and churn insights
- Redesigned Spark logic implementing modular transformations
- Output CSV or printed DataFrame summarizing final business metrics
- Optional visualizations or graphs based on trends



## 📸 Evidence

![dataset_preview.png](./evidence/dataset_preview.png)  
Screenshot of Spark DataFrame showing preview of cleaned dataset

![report_output.png](./evidence/report_output.png)  
Screenshot of final aggregated output file contents

![spark_job_dag.png](./evidence/spark_job_dag.png)  
Screenshot of Spark job DAG representing execution flow

![transformation_logic.png](./evidence/transformation_logic.png)  
Screenshot of code applying business logic transformations




## 📎 Deliverables

- [`- Spark notebook implementing redesign of post-sales reporting pipeline`](./deliverables/- Spark notebook implementing redesign of post-sales reporting pipeline)

- [`- Transformed sales and customer churn datasets`](./deliverables/- Transformed sales and customer churn datasets)

- [`- Final CSV output file summarizing key metrics stored in /deliverables/`](./deliverables/- Final CSV output file summarizing key metrics stored in /deliverables/)

- [`- Summary notes discussing redesign choices and business rationale`](./deliverables/- Summary notes discussing redesign choices and business rationale)

- [`- README with project overview, run steps, and data description`](./deliverables/- README with project overview, run steps, and data description)




## 🛠️ Architecture
- Spark-based data pipeline
- Input CSV files loaded into Spark DataFrames
- PySpark transformations for cleaning, deriving, and aggregating data
- Output in-memory or exported as CSV
- No complex orchestration or external dependencies



## 🔍 Monitoring
- Manual inspection of Spark job DAG
- Printed output or CSV validation
- Spark UI optional for stage-level review
- Compare before-and-after results using summary statistics



## ♻️ Cleanup
- Delete temporary or intermediate DataFrames
- Clean up workspace files or staging outputs
- Save only final outputs and the refined notebook in the repository



*Generated automatically via Python + Jinja2 + SQL Server table `tblMiniProjectProgress` on 09-15-2025 19:26:56*