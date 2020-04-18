### A common task in shell scripting is to parse command line arguments to your script. Bash provides the getopts built-in function to do just that. 

```
#!/bin/bash
while getopts ":ht" opt; do
  case ${opt} in
    h ) # process option a
      ;;
    t ) # process option t
      ;;
    \? ) echo "Usage: cmd [-h] [-t]"
      ;;
  esac
done
```
