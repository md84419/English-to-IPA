#!/usr/bin/awk -f

# USAGE:
#   awk -f txt_to_json.awk en_UK.txt > ../Open_dict.json

BEGIN {
  FS="\t"
  SYMBOLS_FILE = "opendict.symbols.txt"
  print("{");
  while((getline t < ARGV[1]) > 0)last++;close(ARGV[1]);
  while((getline line < SYMBOLS_FILE) > 0) {
    l = length(line);
    if ( l==1 ) {
      symbols1[++count] = line;
    } else if ( l == 2 ) {
      symbols2[++count] = line;
    } else if ( l == 3 ) {
      symbols3[++count] = line;
    }
  }
  close(SYMBOLS_FILE);
  #for(i in symbols1) print symbols1[i];
}
{
  for(i=1;i<NF;i++) {
    printf("\"%s\": ", $i);
  }
  $NF=sprintf("[\"%s\"]",$NF);
  sub(/\[\"\//, "[\"", $NF);
  sub(/\/\"\]/, "\"]", $NF);

  #insert spaces after each symbol
  for(i in symbols3) sub(symbols3[i], symbols3[i]" ", $NF);
  for(i in symbols2) sub(symbols2[i], symbols2[i]" ", $NF);
  for(i in symbols1) sub(symbols1[i], symbols1[i]" ", $NF);

  if( last==FNR ) {
    printf("%s\n",$NF);
  } else {
    printf("%s,\n",$NF);
  }
}
END {
  print("}");
}
