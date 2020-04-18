### Find large files
```
find . -type f -size +1M
```
### Find recently modified files
```
find ~ -mmin -100
```
### Find and update files and directories in a shared directory
```
$ find . -user [you] ! -group [grp]
$ find . -user [you] ! -group [grp] -exec chgrp [yourgroup] {} \;

$ find . -user [you] -perm /u+r ! -perm /g+r
$ find . -user [you] -perm /u+r ! -perm /g+r -exec chmod g+r {} \;

$ find . -user [you] -perm /u+x ! -perm /g+x
$ find . -user [you] -perm /u+x ! -perm /g+x -exec chmod g+x {} \;
```
### Find newest and oldest files in a directory tree
```
find . -type f -printf '%Tc %p\n' | sort -nr | head
find . -type f -printf '%Tc %p\n' | sort -nr | tail
```
### Find biggest and smallest files
```
find . -type f -printf '%k %p\n' | sort -nr | head
find . -type f -printf '%k %p\n' | sort -nr | tail
```
### Find empty directories
```
find . -type d -empty -printf "%Tc %p\n"
```
