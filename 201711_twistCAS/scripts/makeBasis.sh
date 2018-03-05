#!/bin/sh

declare -a basisSet=('cc-pVDZ' 'cc-pVTZ' 'aug-cc-pVDZ' 'aug-cc-pVTZ')
declare -a basisSetNames=('ccpVDZ' 'ccpVTZ' 'augccpVDZ' 'augccpVTZ')

declare -a functional=('lda' 'pbe' 'b3lyp' 'm06')

for i in *.inp
do
  IFS='_'
  newNameArray=( $i )
  for j in {1..3}
  do
    IFS=''
    newName=${newNameArray[0]}_${basisSetNames[$j]}_${newNameArray[2]}_${newNameArray[3]}_${newNameArray[4]}_${newNameArray[5]}.tmp
    cp $i $newName
    sed -i "s/${basisSet[0]}/${basisSet[$j]}/g" $newName
  done
done

for i in *.tmp
do
  updateName=$(echo $i | cut -f 1-2 -d '.')
  mv $i $updateName
done


