#!/usr/bin/python

# USAGE:
#  PYTHONPATH=".." python opendict_to_json.py ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json

import csv, getopt, json, io, os, re, sys, subprocess
from signal import signal, SIGPIPE, SIG_DFL
from eng_to_ipa import tokenize

signal(SIGPIPE, SIG_DFL)


def main(argv):
  input_file = None
  output_file = None
  
  try:
    opts, args = getopt.getopt(argv, "o:")
  except getopt.GetoptError:
    print( "{0}: syntax: [-o output.json] input.csv".format( sys.argv[0]) )
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-o':
      output_file = arg

  try:
    input_file = args[0]
  except:
    print( "{0}: syntax: [-o output.json] input.csv".format( sys.argv[0]) )
    sys.exit(2)

  britfone_dict = {}
  with open('../eng_to_ipa/resources/Britfone_source_files/britfone.main.3.0.1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for rows in reader:
      k = rows[0]
      v = rows[1].strip()
      
      # fix 3.0.1 source
      if k == 'AYE(1)': k = 'AYE'
      if k == 'YOB(1)': k = 'YOB'
      if k == 'PROJECTS(2)': k = 'PROJECTS(1)'
      if k == 'PROJECTS(3)': k = 'PROJECTS(2)'
      
      # Map phonetic to phonemic
      v = v.replace("ˈɐ", "ˈʌ")
      v = v.replace("ˌɐ", "ˌʌ")
      v = v.replace("ɐ", "ʌ")
      
      k = k.lower()
      v = v.lower()
      
      britfone_dict.update( {k: [v]} )

  if( output_file != None ):
    try:
      with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                         '..','eng_to_ipa','resources',output_file), 'wb') as o_fp:
        json.dump( britfone_dict, o_fp, check_circular=True, indent=None, sort_keys=True, separators=[',\n', ':'], ensure_ascii=False )
      sys.exit(0)
    except TypeError:
      pass
  j = json.dumps( britfone_dict, check_circular=True, indent=None, separators=[',', ': '], sort_keys=True, ensure_ascii=False )
  j = re.sub("{", "{\n", j)
  j = re.sub("],", "],\n", j)
  j = re.sub("]}", "]\n}", j)
  print( j )
  sys.exit(0)

if( __name__ == "__main__"):
  main(sys.argv[1:])
