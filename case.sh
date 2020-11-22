

```sh
#!/bin/bash

echo "Input an animal name:  "
read animal

#animal=cat

case $animal in
  dog)
    echo "This is a dog"
    ;;
  cat)
    echo "This is a cat"
    ;;
  fish)
    echo "This is a fish"
    ;;
  *)
    echo "This is not on my list"
    ;;
esac
```

