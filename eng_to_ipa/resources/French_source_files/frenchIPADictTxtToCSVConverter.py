import os
import pathlib
import csv

#setting cwd to path of this file
current_path = pathlib.Path(__file__).parent.absolute()
os.chdir(current_path)

f = open('FR-IPA_Dictionary .txt','r')
print(f.read())