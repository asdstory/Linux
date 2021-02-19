# This is to selectly mv some files to new folder, based on the data modified. 

- [ ] mkdir st001

```sh
# for i in `ls -lrt | grep "Feb 19" | awk '{print $10}' `; do mv $i* ./st001/; done
```

## Make directory in batch and mv corresponding files into the directory.


```sh
# for i in `ls -lrt | awk -F "[. \t]" '{print $9}' `; do mkdir $i; do mv $i.* ./$i/; done
```
