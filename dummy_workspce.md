# Julius Dummy Workspace

This is a dummy repository for testing Julius GitHub connector.

It contains:
- Sample sales data
- Simple Python scripts
- Open issues and pull requests

- Month,Revenue
January,1000
February,1200
March,0
April,1500

import csv

def validate_totals(file):
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Revenue"]) < 0:
                print("Error: Negative revenue found in", row["Month"])
            else:
                print("Revenue OK for", row["Month"])

validate_totals("data/sales.csv")

