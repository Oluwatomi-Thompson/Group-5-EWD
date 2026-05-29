#!/bin/bash
# This script runs the ETL process for the EWD project
# Step 1: Extract data from the source (e.g., JSON files)
echo "Extracting data from source..."

echo "================================"
echo "Running XML ETL process..."
echo "================================"

python etl/run_etl.py

if [ $? -ne 0 ]; then
    echo "ETL process completed successfully."

    else 
    echo "ETL process failed. Please check the logs for details."
    exit 1
fi


