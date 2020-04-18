### Find only that which matched

- [ ] ls -l /home | grep -o "Jan  *[[:digit:]] ..:.."

### Recursive search

- [ ] grep -R -l bash *

### Use a list of matches from a file

- [ ] grep -f complex.grep –h *

### egrep
#### Extended grep allows additional metacharacters like +, ?, |, {} and ()
```
egrep 'ftp/data/[^\/]+/exome_alignment/[^\/]+\.mapped\.ILLUMINA\.bwa\.[^\/]+\.exome\.[^\/]+\.bam' /fdb/1000genomes/ftp/current.tree
```
#### {} match number of times
```
ls -l /home | egrep --color ' [0-9]{7} [[:alpha:]]{3} [0-9]{2}'
```
