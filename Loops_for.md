# Loops - for:

## for .. do .. done

### Usage 1: 
```
for name in words
do
  commands
done
```

### Usage 2: 
```
for (( expr1 ; expr2 ; expr3 ))
do
  commands
done
```

### for is used to step through multiple words
```
for i in apple pear fig ; do echo $i ; done
```
### With brace expansion:
```
for i in {1..5}; do echo $i ; done
```
### With arrays
```
array=(moe larry curly)
for i in "${array[@]}" ; do echo $i ; done
```

### Walk Through Directories
#### Find all files in /home and count how many lines are in each file:
```
for file in $(ls -a ~/); do
[[ -f ~/$file ]] && wc -l ~/$file
done
```

### C-style for loop
#### for can be used for integer  travers
```
for (( i=1 ; i < 2000 ; i=i+i ))
do
echo $i
done
```

