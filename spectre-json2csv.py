import json
import requests
import glob
from datetime import datetime
import csv

# Load environment variables
with open('env.json') as jsonFile:
    env = json.load(jsonFile)

# Call Spectre API and retrieve transaction files
headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'App-id': env['APP_ID'],
    'Secret': env['SECRET'],
    'Customer-secret': env['CUSTOMER_SECRET'],
    'Login-secret': env['LOGIN_SECRET']
    }

accounts = requests.get('https://www.saltedge.com/api/v4/accounts', headers = headers)
for account in accounts.json()['data']:
    transactions = requests.get('https://www.saltedge.com/api/v4/transactions?account_id=' + account['id'], headers = headers)
    if len(transactions.json()['data']) != 0:
        with open('json/' + account['id'] + account['extra']['account_name'] + '.json', 'w') as jsonFile:
            json.dump(transactions.json()['data'], jsonFile)
        nextTransactionId = transactions.json()['meta']['next_id']
        while nextTransactionId:
            transactions = requests.get('https://www.saltedge.com/api/v4/transactions?account_id=' + account['id'] + '&from_id=' + str(nextTransactionId), headers = headers)
            with open('json/' + account['id'] + account['extra']['account_name'] + str(nextTransactionId) + '.json', 'w') as jsonFile:
                json.dump(transactions.json()['data'], jsonFile)
            nextTransactionId = transactions.json()['meta']['next_id']

# Create array of JSON files to parse
jsonFilePaths = glob.glob('json/*.json')

# Per JSON file
for jsonFilePath in jsonFilePaths:

    # Open file and read metadata
    with open(jsonFilePath) as jsonFile:
        transactions = json.load(jsonFile)
        account = transactions[0]['account_id']
        closingDate = transactions[len(transactions) - 1]['made_on']

        # Generate corresponding CSV file with header row
        with open('csv/' + str(account) + '-' + closingDate + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(['Account ID', 'Amount', 'Currency', 'Date', 'Info', 'Reference'])

            # Write each transaction as row in CSV file
            for transaction in transactions:
                writer.writerow([account, transaction['amount'], transaction['currency_code'], transaction['made_on'], transaction['description'], transaction['id']])
