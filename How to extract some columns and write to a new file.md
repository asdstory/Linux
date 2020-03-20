### How to print/extract some of the columns we want, and put it into a new file.

- [ ] awk NR >18 '{print $1, $9 > "micrographs_ctf_test.star"} ' micrographs_ctf.star
