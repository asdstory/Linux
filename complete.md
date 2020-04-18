### Tab-complete possible arguments
```
function do_something { echo You picked $1; }

complete -W "this that the_other" do_something

complete -f -X '!*.out' do_something

```
