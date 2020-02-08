### This shell command is used to select micrographs after CTF find, read micrographs_ctf.star file and generate a new file containing micrographs with desired resolution:
- [ ] cd to the CTF find results job folder, where micrographs_ctf.star existed.
- [ ] awk '$13 <=4' micrographs_ctf.star > micrographs_ctf_new.star
