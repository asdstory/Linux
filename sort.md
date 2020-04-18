### Sort lines of text by columns of different types
```
ls -l /home | sort -k8,8 -k6,6M -k7,7n
```
### Sort a very large file with a memory limit
```
sort /fdb/annovar/current/hg19/hg19_ljb26_cadd.txt –n –k6 –S 25%
```
