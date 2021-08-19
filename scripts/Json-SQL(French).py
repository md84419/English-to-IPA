import json
from os import chdir
import sqlite3
import re
import os
import pathlib
from sqlite3.dbapi2 import connect
import json

os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
os.chdir('.\\eng_to_ipa\\resources')
with open('fr_Open_Dict.json', 'w',encoding='UTF-8') as fp:
    jsonText = json.load(fp)
    print(jsonText)


os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
os.chdir('.\\eng_to_ipa\\resources')
print(os.getcwd())
connection = sqlite3.connect("fr_FR.db")
cursor = connection.cursor()





connection.commit()
connection.close()