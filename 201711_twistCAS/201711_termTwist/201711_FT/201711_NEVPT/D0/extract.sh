#!/bin/bash

for i in *ccpVD*.out
do
 TOTAL=$(grep "Corrected WF-in-DFT" $i | tr -dc '0-9') 
 NEV=$(grep "Total NEVPT2" $i | cut -c13- | tr -dc '0-9')
 CAS=$(grep "CAS Energy" $i | tr -dc '0-9')
 echo $i
 echo "Total: $TOTAL"
 echo "NEV: $NEV"
 echo "CAS: $CAS"
 echo "CAS TOTAL: $((TOTAL -(NEV - CAS)))"
done
