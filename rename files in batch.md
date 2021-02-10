# This is used to rename multiple files using rename in Linux

- [ ] find . -name '*Aug13' -exec rename Aug13 Aug14 {} +

Or, we can do 

- [ ] rename 's/RhopH-2Pulldown/PNPLA6/' *

Or, use the for loop combined with move

- [ ] for f in *.star; do mv -- "$f" "${f%.star}_DW.star"; done
