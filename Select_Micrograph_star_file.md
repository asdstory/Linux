## This shell command is used to select micrographs based on defocus, Astigmatism, and Maxresolution. 

#### After finished CTF find using RELION. Use following command to micrographs_ctf.star file and generate a new star file containing micrographs with desired defocus (5000<=rlnDefocusU<=3000), Astigmatism (rlnCtfAstigmatism<1000), and resolution(rlnCtfMaxResolution <=4):


- [ ] cd to the CTF find results job folder, where micrographs_ctf.star exists.
- [ ] awk 'NR <= 18 {print $0 > "micrographs_ctf_new.star"} NR >18 && $3 >= 5000 && $3 <=30000 && $5 <= 1000 && $13 <=4 {print $0 >> "micrographs_ctf_new.star"}' micrographs_ctf.star

### Note: 
- You can also change any of the thresold to get desired micrograph, e.g. default resolution thresold is 4, but you can change it to 5 to select more micrographs.
- When trying to extract particles from selected micrographs using RELION, you will find that RELION only show "micrographs_ctf.star" in the default I/O. In the I/O panel, just select "micrographs_ctf.starCtfFind/job002/micrographs_ctf.satr" and change it to "CtfFind/job002/micrographs_ctf_new.star". In this way, you will extract particles only from micrographs you just selected. 


### More detail about the awk command:
https://likegeeks.com/awk-command/
http://blog.cee.moe/a-brief-introduction-to-grep-awk-and-sed.html
