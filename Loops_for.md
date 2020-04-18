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
