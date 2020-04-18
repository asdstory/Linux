### Basic usage:
```
while test-commands
do
  consequent-commands
done
```
### Example:
```
a=1
while [[ $a -le 5 ]] ; do echo $a ; ((a++))  ; done
```

### Similar loops: until .. do .. done
```
until test-commands
do
  consequent-commands
done
```
