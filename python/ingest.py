import json
import xml.etree.ElementTree as ET
import pandas as pd

def load_credit_bureau(xml_file):
    tree = ET.parse(xml_file)
    return tree.getroot()

def load_fraud_api(json_file):
    with open(json_file) as f:
        return json.load(f)

def load_customer(csv_file):
    return pd.read_csv(csv_file)

print("Data ingestion completed successfully.")
