# Adding a language to the Cued Speech Service API


## Overview
The Cued Speech Service uses Robotica's fork of the Python English-to-IPA service (at the time of writing, v0.3.a18).  The [requirements.txt](https://dev.azure.com/roboticaml/Cued-Speech/_git/Cued-Speech?path=/requirements.txt) file specifies the requirement and the use of the test pypi directory to locate the module.  The source to the fork of English-to-IPA can be found at https://github.com/md84419/English-to-IPA​



## English-to-IPA
The GB and US dictionaries live in /eng_to_ipa/resources/  To add support for another language, we need to add the language file with the correct name and contents, as a .db and as a .json file.

The GB and US disctionaries are built from Britfone, Open Dict and CMU.  We fork, extend and convert these two dictionaries to create the .db and .json dictionaries in the correct formats.

The source Britfone dictionary is /eng_to_ipa/resources/Britfone_source_files/

The source Openddict dictionary is /eng_to_ipa/resources/Opendict_source_files/



### Converting
To convert for English language, we:

1. Use /scripts/britfonedict_to_json.py to convert Britfone's csv file to json
2. Use /scripts/opendict_to_json.py to convert Britfone's csv file to json
3. Use /scripts/cmudict_to_json.py to convert CMU's csv file to json
4. Use /scripts/create_en_US_dict.py to produce the en_US.json dictionary
5. Use /scripts/create_en_GB_dict.py to produce the en_GB.json dictionary
6. Use /scripts/cmudict_to_sql.py to convert the CMU json file into a .db file
7. Use /scripts/dict_to_sql.py to convert the GB and US json files into .db files
There is a convenience script, /scripts/rebuild_all.sh , which does all the above in order


### Robotica's extensions
1. We standardise the IPA sourced from the Britfone and Open dictionaries.
    1. In /scripts/britfonedict_to_json.py , in main(), we fix a couple of bugs in the 3.0.1 source
    2. In /scripts/britfonedict_to_json.py , in fix_britfone(), we convert the IPA syntax
    3. In /scripts/opendict_to_json.py , in fix_opendict(), we convert the IPA syntax
2. When producing the GB dictionary...
    1. we fix words that incorrectly start with '^', in /scripts/create_en_GB_dict.py fix_opendict()
    2. we fix quadphgraphs and triphthongs, in /scripts/create_en_GB_dict.py fix_gb()
5. When producing the US dictionary...
    1. we standardise the IPA sourced from the CMU dictionary, in  /scripts/create_en_US_dict.py fix_cmu()
2. We change the IPA of certain works, remove other words, and add other words still
    1. For Britfone, in /scripts/britfonedict_to_json.py , in fix_britfone_words()
    2. For Opendict, in /scripts/opendict_to_json.py , in fix_opendict_words()
    3. For GB English, we prefer the Britfone IPA pronounication over the Opendict pronounciation for the (currently 835) words in /eng_to_ipa/resources/Open_dict_drop.json
    4. For US English, in /scripts/create_en_US_dict.py , in fix_US_words()
There are similar functions in create_<lang>_dict.py when creating the .db files

### Adding support for another language
To add support for another language:
1. Create or extend tests in /tests/ to give good test coverage for the new dictionary.  Use the tests for the existing languages as a starting point - you want at least as good a test coverage for your new language as already exists for the current languages - ideally better coverage
2. Source or write the dictionary.  These are good places to start:
    1. https://github.com/open-dict-data/ipa-dict/tree/master/data
    2. https://github.com/Kyubyong/pron_dictionaries
3. Put the source file(s) in their own directory in /eng_to_ipa/resources/ (or in the Opendict_source_files or Britfone_source_files directory if appropriate - be careful not to overwrite any existing file)
4. If you have multiple source files, perhaps from different projects, create new scripts in /scripts which convert to json and normalise the IPA for each before they are combined, if you wish (similar to how we do with the Britfone and Opendict sources).
    1. see /eng_to_ipa/resources/README_dict.md for details of the format, refer to the existing scripts for further guidance.
    2. The json file should be written to /eng_to_ipa/resources/ as <dictionary>_dict.json where <dictionary> is a unique name for this dictionary and language
    3. The script shall be called <dictionary>_to_json.py.
5. Modify or create new scripts in /scripts that will either combine the files from the previous step (if applicable,) or (alternatively) convert the dictionary to json in our in-house IPA format
    1. see /eng_to_ipa/resources/README_dict.md for details of the format, refer to the existing scripts for further guidance.
    2. The json file should be written to /eng_to_ipa/resources/ as <language>.json where <language> is as specified in /README.md
    3. The script shall be called create_<language>_dict.py.  If needed, you can create supporting scripts that offload some of the work
6. Modify or create new scripts in /scripts to produce the .db version, given the .json version  
7. Be sure to update /scripts/rebuild_all.sh to include the scripts for the new language​
