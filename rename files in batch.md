# This is used to rename multiple files using rename in Linux

We can use find to achieve/implement this function:

- [ ] find . -name '*Aug13' -exec rename Aug13 Aug14 {} +

we can also use rename 

- [ ] rename 's/RhopH-2Pulldown/PNPLA6/' *

Or, use the "for" loop combined with "move"

- [ ] for f in *.star; do mv -- "$f" "${f%.star}_DW.star"; done

*Note: Try modify "*.star" and "{f%.star}_DW.star" part to comply your request. 
