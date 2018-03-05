#/bin/sh

for folder in *ane
do
 cd $folder/*react*/*freeze*
 rm *.err
 rm *.log
 rm *.out
 for file in *.inp
 do
  sed -i 's/cycles 100/cycles 300/g' $file
  sed -i 's/#shift/shift/g' $file
  sed -i 's/#damp/damp/g' $file
  qsub ${file%.inp}.pbs
 done
 cd ../../*prod*/*freeze*
 rm *.err
 rm *.log
 rm *.out
 for file in *.inp
 do
  sed -i 's/cycles 100/cycles 300/g' $file
  sed -i 's/#shift/shift/g' $file
  sed -i 's/#damp/damp/g' $file
  qsub ${file%.inp}.pbs
 done
 cd ../../../
done

