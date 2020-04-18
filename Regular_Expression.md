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

An online tool:

https://regexr.com/
