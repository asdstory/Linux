### continue - Can be used to skip to next element
```
for a in {1..5}; do 
  if [[ $a == 2 ]]; then 
    continue; 
  fi
  echo $a
done
```

### break - Can be used to end loops or skip sections
```
a=1
while [[ 1 ]] ; do 
  echo $a
  if (( a > $(date +%s) )) ; then
    break
  fi
  (( a=a+a ))
done
```
