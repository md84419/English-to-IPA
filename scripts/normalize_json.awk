#!/bin/awk -f

# USAGE:
#   awk -f normalize_json.awk CMU_dict.json> en_US.json

BEGIN {
  FS="], "
  while((getline t < ARGV[1]) > 0)last++;close(ARGV[1])
  print "{"
}
{
  for(i=1;i<NF;i++) {
    sub(/^{/, "", $i)
    $i=$i"],"
    printf("%s\n", $i);
  }
  sub(/}$/, "", $NF)
  printf("%s\n",$NF);
}
END {
  print "}"
}
