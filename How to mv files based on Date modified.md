# This is to selectly mv some files to new folder, based on the data modified. 

- [ ] mkdir st001

```sh
# for i in `ls -lrt | grep "May 12" | awk '{print $10}' `; do mv $i* /st001/; done
```

