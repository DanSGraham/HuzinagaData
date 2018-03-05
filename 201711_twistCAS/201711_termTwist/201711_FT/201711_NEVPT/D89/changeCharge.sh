#!/bin/sh

#To be run within the folder to change the charges

for f in *4.inp
do
sed -i 's/charge +1/charge -1/g' $f
sed -i '0,/charge -1/{s/charge -1/charge +1/}' $f
done
