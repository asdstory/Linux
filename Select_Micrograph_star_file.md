### This shell command is used to select micrographs after CTF find based on defocus, Astigmatism, and Maxresolution. It will read micrographs_ctf.star file and generate a new star file containing micrographs with desired defocus (5000<=rlnDefocusU<=3000), Astigmatism (rlnCtfAstigmatism<1000), and resolution(rlnCtfMaxResolution <=4):
*You can also change any of the thresold to get desired micrograph, e.g. default resolution thresold is 4, but you can change it to 5 to select more micrographs.* 

- [ ] cd to the CTF find results job folder, where micrographs_ctf.star existed.
- [ ] awk 'NR <= 18 {print $0 > "micrographs_ctf_new.star"} NR >18 && $3 >= 5000 && $3 <=30000 && $5 <= 1000 && $13 <=4 {print $0 >> "micrographs_ctf_new.star"}' micrographs_ctf.star


### More detail about the awk command:
https://likegeeks.com/awk-command/
http://blog.cee.moe/a-brief-introduction-to-grep-awk-and-sed.html
