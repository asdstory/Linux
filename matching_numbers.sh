#!/usr/bin/bash

echo -n "Type in something :  "
read response
echo "You said: $response"

if [[ "$response" == [0-9][0-9][0-9] ]] ; then
  echo "This is a three-digit number!"
elif $( echo "$response" | grep -q "^[0-9]\+$" ) ; then
  echo "This is an integer!"
elif $( echo "$response" | grep -q "^[0-9]\+\.[0-9]*$" ) ; then
  echo "This is a floating point number!"
elif $( echo "$response" | egrep -q '^(\+|-)?[0-9]+\.?[0-9]+(e\+[0-9]+|e-[0-9]+|e[0-9]+)?$'  ) ; then
  echo "This is scientific notation!"
else
  echo "I don't know what to say..."
fi
