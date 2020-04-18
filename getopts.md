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

```
#!/bin/bash
mem="lg"
tmpdir="/tmp"
usage="$0 [-m] [-t] [-h]

    -m mem (default lg)
    -t tmpdir (default /tmp)
    -h show this help menu"

while getopts "m:t:h" flag; do
  case "$flag" in
    m) mem=$OPTARG ;;
    t) tmpdir=$OPTARG ;;
    h) echo "usage" ; exit 0 ;;
    ?) echo "usage" ; exit 1 ;;
  esac
done
```

