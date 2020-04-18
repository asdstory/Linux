### Allow more precise matching

Only enabled with =~ operator

```

x=fig
[[ $x =~ ^f[io]g$ ]] && echo this is probably fig
[[ ! $x =~ ^d[io]g$ ]] && echo huh?

```
### Allows capturing of submatches

```

y=123.456.7890
[[ $y =~ ^([0-9]+)\.[0-9]{3}\.[0-9]{4}$ ]] &&
  echo ${BASH_REMATCH[1]}

```

### Can capture a submatch using () and $BASH_REMATCH array

```
str="The quick red fox jumped over the lazy brown dog"

if [[ $str =~ quick\ (.*)\ fox ]] ; then
  echo Total match: ${BASH_REMATCH[0]}
  echo Submatch:    ${BASH_REMATCH[1]}
fi

```


An online tool:

https://regexr.com/
