#!/bin/sh

declare -a basisSet=('3-21g' '6-311g' 'cc-pVDZ' 'cc-pVTZ' 'aug-cc-pVDZ' 'aug-cc-pVTZ')
declare -a basisSetNames=('321g' '6311g' 'ccpVDZ' 'ccpVTZ' 'augccpVDZ' 'augccpVTZ')

declare -a functional=('lda' 'pbe' 'b3lyp' 'm06')

for i in *.inp
do
  IFS='_'
  newNameArray=( $i )
  for j in {1..5}
  do
    IFS=''
    newName=${newNameArray[0]}_${basisSetNames[$j]}_${newNameArray[2]}_${newNameArray[3]}_${newNameArray[4]}_${newNameArray[5]}.tmp
    cp $i $newName
    sed -i "s/3-21g/${basisSet[$j]}/g" $newName
  done
done

for i in *.tmp
do
  updateName=$(echo $i | cut -f 1-2 -d '.')
  mv $i $updateName
done


