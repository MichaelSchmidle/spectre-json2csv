import os
import glob
import json
from datetime import datetime
import csv

# Determine base directory of this script
baseDir = os.path.dirname(__file__) + '/'

# Create array of JSON files to parse
jsonFilePaths = glob.glob(baseDir + 'json/*.json')

# Per JSON file
for jsonFilePath in jsonFilePaths:

    # Open file and read metadata
    with open(jsonFilePath) as jsonFile:
        transactions = json.load(jsonFile)
        account = transactions[0]['account_id']
        closingDate = transactions[len(transactions) - 1]['made_on']

        # Generate corresponding CSV file with header row
        with open(baseDir + 'csv/' + str(account) + '-' + closingDate + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['Account ID', 'Amount', 'Currency', 'Date', 'Info', 'Reference'])

            # Write each transaction as row in CSV file
            for transaction in transactions:
                writer.writerow([account, transaction['amount'], transaction['currency_code'], transaction['made_on'], transaction['description'], transaction['id']])

