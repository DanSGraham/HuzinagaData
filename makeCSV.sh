#!/bin/sh

#To be run within a folder

cd *reactant
cd *freezeAndThaw
for f in *.out
do
echo $f
done
cd ../../
cd *trans*
cd *freeze*
for f in *.out
do
echo $f
done
cd ../../

