### Using select for menus

```
#!/bin/bash

echo "Pick a fruit, any fruit"

select fname in apple pear fig plum pineapple orange
do
  break
done

echo "You picked $fname"
```
