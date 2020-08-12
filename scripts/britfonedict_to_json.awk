#!/bin/awk -f

# USAGE:
#   awk -f csv_to_json.awk ../eng_to_ipa/resources/Britfone_source_files/britfone.main.3.0.1.csv > ../eng_to_ipa/resources/Britfone_dict.json

BEGIN {
  FS=", "
  print("{");
  while((getline t < ARGV[1]) > 0)last++;close(ARGV[1]);
}
{
  for(i=1;i<NF;i++) {
    # fix 3.0.1 source
    sub(/^AYE\(1\)/, "AYE", $i);
    sub(/^YOB\(1\)/, "YOB", $i);
    sub(/^PROJECTS\(2\)/, "PROJECTS(1)", $i);
    sub(/^PROJECTS\(3\)/, "PROJECTS(2)", $i);
    
    $i=tolower($i);
    printf("\"%s\": ", $i);
  }
  if( last==FNR ) {
    printf("[\"%s\"]\n",$NF);
  } else {
    printf("[\"%s\"],\n",$NF);
  }
}
END {
  print("}");
}
