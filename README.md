# Spectre JSON to CSV Converter

The script spectre-json2csv.py converts—as its name suggests—JSON files provided by [Spectre](https://www.saltedge.com/products/spectre) to simple CSV files.

To start, copy the file ``default.env.json`` to ``env.json`` and provide the required variables to connect to the Spectre API. Then run the script with the command ``$ python spectre-json2csv.py``. The JSON files retrieved from the API are place in the subfolder ``json`` and subsequently will be converted into CSV files in the ``csv`` subfolder.
