#!/bin/bash

# Activate Python virtual environment (optional)
source ~/pyspark_venv/bin/activate

# Remove old output directory if it exists
rm -rf output

# Submit the Spark job
spark-submit autoinc_spark.py

# Deactivate virtual environment
deactivate