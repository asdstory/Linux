#!/bin/bash
module load bowtie
for i in {1..22} X Y M ; do
  label=$i
  if [[ $i == [[:digit:]] ]]; then
    label=$(printf '%02d' $i)
  fi
  [[ -f x/$label/trial.out ]] && break
  [[ -d x/$label ]] || mkdir -p x/$label
  pushd x/$label 2>&1 > /dev/null
  echo Running chr${i}_out 
  # actually do something, not this
  touch trial_chr${i}.out
  popd >& /dev/null
done
