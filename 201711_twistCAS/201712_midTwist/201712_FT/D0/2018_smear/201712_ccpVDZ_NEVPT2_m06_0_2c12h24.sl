#!/bin/bash
#SBATCH -J 201712_ccpVDZ_NEVPT2_m06_0_2c12h24
#SBATCH -N 1
#SBATCH -t 00:10:00
#SBATCH -e /global/u1/d/dgraham/mesabi_stuff/HuzinagaData/201711_twistCAS/201712_midTwist/201712_FT/D0/2018_smear/201712_ccpVDZ_NEVPT2_m06_0_2c12h24.err
#SBATCH -o /global/u1/d/dgraham/mesabi_stuff/HuzinagaData/201711_twistCAS/201712_midTwist/201712_FT/D0/2018_smear/201712_ccpVDZ_NEVPT2_m06_0_2c12h24.out
#SBATCH -C knl,quad,cache
#SBATCH -q debug

module load python/3.6-anaconda-4.4
export OMP_NUM_THREADS=8
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

export HDF5_USE_FILE_LOCKING=FALSE

source activate myenv
python /global/homes/d/dgraham/mesabi_stuff/HuzinagaData/code/python/freeze_and_thaw/cython/cmain.py /global/u1/d/dgraham/mesabi_stuff/HuzinagaData/201711_twistCAS/201712_midTwist/201712_FT/D0/2018_smear/201712_ccpVDZ_NEVPT2_m06_0_2c12h24.inp

