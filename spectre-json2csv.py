import json

# Determine base directory of this script
baseDir = os.path.dirname(__file__) + '/'

# Create array of JSON files to parse
jsonFiles = glob.glob(baseDir + 'json/*.json')

# Per JSON file
for jsonFile in jsonFiles:

    # Define metadata
    iban = 
    owner = 
    closingDate = 

    # Generate corresponding CSV file with header row
    with open(baseDir + 'csv/' + iban + '-' + closingDate + '.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['IBAN', 'Owner', 'Amount', 'Currency', 'Date', 'Info', 'Reference'])
        
        for transaction in transactions:
            amount =
            currency = 
            date = 
            info = 
            reference = 

            # Write transaction row to CSV file
            writer.writerow([iban, owner, amount, currency, date, info, reference])
