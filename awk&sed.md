### awk is a scripting language
```
awk '{sum += $2} END {print sum/NR}' file_for_sorting.txt
```
### sed is a file/stream manipulation language
```
sed 's/Feb/February/g' file_for_sorting.txt
sed -n '5,8p' file_for_sorting.txt
```
