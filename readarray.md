### Read a file into an array
```
$ cat file_to_be_mapped.txt
This is line one
The second line
Finally line 3
$ readarray zzz < file_to_be_mapped.txt
$ echo ${zzz[1]}
The second line
```
### Sort elements of an array
#### Use xargs
```
array=(apple pear fig plum pineapple orange)
echo ${array[@]} | xargs -n 1 | sort | xargs
apple fig orange pear pineapple plum

```
### Unique sorted elements
```
array=(3 0 4 7 0 8 4 5 9 6 3 1 9 0 2 3 4)
echo ${array[@]} | xargs -n 1 | sort -u | xargs
0 1 2 3 4 5 6 7 8 9
```
