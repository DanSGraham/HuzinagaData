#!/bin/sh


for folder in *ane
do
 cd $folder/*react*/*CCSDT
 rm *.err
 rm *.log
 rm *.out
 for file in *.pbs
 do
  qsub $file
 done
 cd ../../*trans*/*CCSDT
 rm *.err
 rm *.log
 rm *.out
 for file in *.pbs
 do
  qsub $file
 done
 cd ../../..
done
