import os
import glob
import json
from datetime import datetime
import csv

# Determine base directory of this script
baseDir = os.path.dirname(__file__) + '/'

# Create array of JSON files to parse
jsonFiles = glob.glob(baseDir + 'json/*.json')

# Per JSON file
for jsonFile in jsonFiles:

    print(jsonFile)
