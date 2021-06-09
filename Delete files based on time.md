### Find files older/newer than xx time, and remove them.
```sh
find . -mtime -1 -exec ls {} \;

find . -mtime -1 -exec rm -rf {} \;
```
