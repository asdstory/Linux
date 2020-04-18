 If you set shopt -s extglob then you can also use extended pattern matching:

?() - zero or one occurrences of pattern
*() - zero or more occurrences of pattern
+() - one or more occurrences of pattern
@() - one occurrence of pattern
!() - anything except the pattern

```

shopt -s extglob
for arg in apple be cd meet o mississippi
do
    # call functions based on arguments
    case "$arg" in
        a*             ) foo;;    # matches anything starting with "a"
        b?             ) bar;;    # matches any two-character string starting with "b"
        c[de]          ) baz;;    # matches "cd" or "ce"
        me?(e)t        ) qux;;    # matches "met" or "meet"
        @(a|e|i|o|u)   ) fuzz;;   # matches one vowel
        m+(iss)?(ippi) ) fizz;;   # matches "miss" or "mississippi" or others
        *              ) bazinga;; # catchall, matches anything not matched above
    esac
done

```
