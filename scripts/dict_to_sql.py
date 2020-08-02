# Script for converting the dictionary json file to an SQL table
import ast
import sqlite3
import json
import re
import unittest
from os.path import join, abspath, dirname

conn1 = sqlite3.connect(join(abspath(dirname(__file__)), '..', 'eng_to_ipa', 'resources', 'en_GB.db'))
f1 = 'en_GB.json'
c1 = conn1.cursor()

conn2 = sqlite3.connect(join(abspath(dirname(__file__)), '..', 'eng_to_ipa', 'resources', 'en_US.db'))
f2 = 'en_US.json'
c2 = conn2.cursor()


def create_dictionary_table(tu):
    c,conn,f = tu
    try:
        c.execute("""CREATE TABLE dictionary 
                    (id INTEGER PRIMARY KEY,
                    word text NOT NULL,
                    phonemes text NOT NULL
                    )""")
        conn.commit()
    except sqlite3.OperationalError:
        c.execute("DROP TABLE dictionary;")
        conn.commit()
        create_dictionary_table(tu)


def insert_dictionary_values(tu):
    """takes the prepared data and places it into the database"""
    c,conn,f = tu
    dictionary_data = []
    with open(join(abspath(dirname(__file__)), '..', 'eng_to_ipa', 'resources', f), encoding="UTF-8") as source_file:
        mydict = json.load( source_file )
        for word,phonemes in mydict.items():
            if( isinstance( phonemes, list )):
                phonemes = str( phonemes )
            dictionary_data.append((word, phonemes))
    c.executemany("INSERT INTO dictionary(word, phonemes) VALUES (?, ?)", dictionary_data)
    conn.commit()

    # test sanity - do we get out what we put in?
    tc = unittest.TestCase()
    testwords = ["aardvark", "teacher"]
    for word in testwords:
        t = mydict[word]
        c.execute("SELECT phonemes FROM dictionary WHERE word = \"{0}\"".format(word) )
        r = c.fetchone()[0]
        r = ast.literal_eval( r )
        tc.assertEqual( t, r )


if __name__ == "__main__":
    for tu in [[c1, conn1, f1], [c2, conn2, f2]]:
        create_dictionary_table(tu)
        insert_dictionary_values(tu)
        # small test to verify valid database creation:
        tu[0].execute("SELECT * FROM dictionary WHERE word like \"%str%\"")
        for r in tu[0].fetchall():
            print(str(r))
