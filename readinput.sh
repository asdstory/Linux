while read var
do
  if [[ $var == "exit" ]]
  then
    break
  fi
  echo $var
  # do something else with $var
done
