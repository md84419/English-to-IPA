import csv
import json
import os
import pathlib
import time

os.chdir(pathlib.Path(__file__).parent.absolute())
csvFilePath = 'FR-IPA_Dictionary.csv'
jsonFilePath = 'FR-IPA_Dictionary.json'

with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    for rows in csvReader:
        print(rows)
        print(time.sleep(1))
    #     # Convert each row into a dictionary
    #     # and add it to data

             
    #         # Assuming a column named 'No' to
    #         # be the primary key
    #         key = rows['No']
    #         data[key] = rows
 
    # # Open a json writer, and use the json.dumps()
    # # function to dump data
    # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    #     jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Decide the two file paths according to your
# computer system

 
# Call the make_json function
# make_json(csvFilePath, jsonFilePath)