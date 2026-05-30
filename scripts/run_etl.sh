#!/bin/bash
# This script runs the ETL process for the EWD project

echo "================================"
echo "Running XML ETL process..."
echo "================================"

python etl/run_etl.py

# Check exit status
if [ $? -eq 0 ]; then
    echo "ETL process completed successfully."
else
    echo "ETL process failed. Please check the logs for details."
    exit 1
fi