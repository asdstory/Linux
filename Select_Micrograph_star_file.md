### This shell command is used to select micrographs after CTF find, read micrographs_ctf.star file and generate a new file containing micrographs with desired resolution, :
- [ ] cd to the CTF find results job folder, where micrographs_ctf.star existed.
- [ ] awk 'NR <= 18 {print $0 > "micrographs_ctf_new.star"} NR >18 && $3 >= 5000 && $3 <=30000 && $5 <= 1000 && $13 <=4 {print $0 >> "micrographs_ctf_new.star"}' micrographs_ctf.star


### More detail about the awk command:
https://likegeeks.com/awk-command/
http://blog.cee.moe/a-brief-introduction-to-grep-awk-and-sed.html
