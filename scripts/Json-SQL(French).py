import json
from os import chdir
import sqlite3
import re
import os
import pathlib
from sqlite3.dbapi2 import connect
import json

def create_dictionary_table():
    try:
        cursor.execute("""CREATE TABLE fr_ipa
                    (word_id INTEGER PRIMARY KEY,
                    word text NOT NULL,
                    ipa text NOT NULL
                    )""")
        connection.commit()
    except sqlite3.OperationalError:
        cursor.execute("DROP TABLE fr_ipa;")
        connection.commit()
        create_dictionary_table()

os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
os.chdir('.\\eng_to_ipa\\resources')
with open('fr_Open_Dict.json', 'r',encoding='UTF-8') as fp:
    jsonText = json.load(fp)
    jsonText = dict(jsonText)
    global words, IPApronociation
    words = list(jsonText.keys())
    IPApronociation = list(jsonText.values())

os.chdir(pathlib.Path(__file__).parent.absolute().parent.absolute())
os.chdir('.\\eng_to_ipa\\resources')
connection = sqlite3.connect("fr_FR.db")
cursor = connection.cursor()
create_dictionary_table()
for i in range(len(words)):
    listToAdd = [i+1,words[i],str(IPApronociation[i])]
    cursor.execute('INSERT INTO fr_ipa (word_id,word,ipa) VALUES (?,?,?)',listToAdd)
connection.commit()
connection.close()