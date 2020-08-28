#!/bin/awk -f

# USAGE:
#   awk -f txt_to_json.awk ../eng_to_ipa/resources/Opendict_source_files/en_UK.txt > ../eng_to_ipa/resources/Open_dict.json

BEGIN {
  FS="\t"
  print("{");
  while((getline t < ARGV[1]) > 0)last++;close(ARGV[1]);
}
{
  for(i=1;i<NF;i++) {
    printf("\"%s\": ", $i);
  }
  $NF=sprintf("[\"%s\"]",$NF);
  sub(/\[\"\//, "[\"", $NF);
  sub(/\/\"\]/, "\"]", $NF);

  if( last==FNR ) {
    printf("%s\n",$NF);
  } else {
    printf("%s,\n",$NF);
  }
}
END {
  print("}");
}
