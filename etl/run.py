
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from dsa.parser import parse_sms_xml
from etl.clean_normalize import clean_sms_data
from etl.categorize import categorize_sms
from etl.load_db import init_db, insert_sms

FILE_PATH = os.path.join(BASE_DIR, "data", "modified_sms_v2.xml")


def run_pipeline():
    try:
        print("Starting ETL pipeline...")

        raw_data = parse_sms_xml(FILE_PATH)
        cleaned = clean_sms_data(raw_data)
        categorized = categorize_sms(cleaned)

        init_db()
        insert_sms(categorized)

        print(f"Pipeline complete: {len(categorized)} records inserted")

    except Exception as e:
        print("Pipeline failed:", str(e))


if __name__ == "__main__":
    run_pipeline()