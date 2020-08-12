#!/bin/bash

# Create json versions of the source dictionaries
awk -f csv_to_json.awk ../eng_to_ipa/resources/Britfone_source_files/britfone.main.3.0.1.csv > ../eng_to_ipa/resources/Britfone_dict.json
PYTHONPATH=".." python opendict_to_json.py ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json
python cmudict_to_json.py

# Create the json language dictionaries
PYTHONPATH=".." python create_en_US_dict.py > ../eng_to_ipa/resources/en_US.json
PYTHONPATH=".." python create_en_GB_dict.py > ../eng_to_ipa/resources/en_GB.json

# Create the db versions
python cmudict_to_sql.py
python dict_to_sql.py
