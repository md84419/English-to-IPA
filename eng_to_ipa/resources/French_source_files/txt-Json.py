import csv
import json
import os
import pathlib
import time

os.chdir(pathlib.Path(__file__).parent.absolute())
txtFilePath = 'FR-IPA_Dictionary.txt'
jsonFilePath = 'FR-IPA_Dictionary.json'

f = open(txtFilePath, "r",encoding='UTF-8')
textDict = {}
text = f.read()
textLineList = text.split('\n')
for i in range(len(textLineList)):
    textLineDictStyleList = textLineList[i].split(',')
    textDict[textLineDictStyleList[0]] = [(textLineDictStyleList[1])]

#print(textDict)

with open(jsonFilePath, 'w',encoding='UTF-8') as fp:
    json.dump(textDict, fp,check_circular=True, indent=None, separators=[',\n', ':'], ensure_ascii=False )