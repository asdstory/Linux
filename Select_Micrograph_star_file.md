### This shell command is used to select micrographs after CTF find, read micrographs_ctf.star file and generate a new file containing micrographs with desired resolution:
- [ ] cd to the CTF find results job folder, where micrographs_ctf.star existed.
- [ ] awk '$3 >= 5000 && $3 <=30000 && $5 <= 1000 && $13 <=4' micrographs_ctf.star > micrographs_ctf_new.star







### Examples about how to use awk:
- [ ] awk -F, '{if($1=="OPTSTK"&&$13>0)print > "stockoptions.csv";}' fo1.csv fo2.csv
- [ ] awk -F, '$1 == "OPTSTK" && $13 > 0 { print >> "stockoptions.csv" }' fo1.csv fo2.csv
- [ ] awk -F, '$1 == "OPTSTK" && $13 > 0' fo1.csv fo2.csv >>"stockoptions.csv"
- [ ] awk '{if ($1 > 30) print $1}' testfile
https://likegeeks.com/awk-command/
### More detail about the awk command:
http://blog.cee.moe/a-brief-introduction-to-grep-awk-and-sed.html
