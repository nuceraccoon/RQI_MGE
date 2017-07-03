#!/bin/bash

#PBS -A nfi106
#PBS -l nodes=3136
#PBS -l walltime=12:00:00
#PBS -o bw1484_rqi.out
#PBS -N Insilico_SN
#PBS -j oe
#PBS -m bea
#PBS -M mrt@ornl.gov
#PBS -q batch

cd $PBS_O_WORKDIR
export HDF5_DISABLE_VERSION_CHECK=1
export MPICH_PTL_MATCH_OFF=1
export LD_LIBRARY_PATH=${HDF5_DIR}/lib:$LD_LIBRARY_PATH
ulimit -c unlimited
export ATP_ENABLED=1

base=$PBS_O_WORKDIR

exe=$PROJWORK/nfi011/Exnihilo/installs/Exnihilo.20161005/bin/neutronics
inp=bw1484_small.xml

date
echo job ID = $PBS_JOBID
echo mpi nodes = $PBS_NUM_NODES
echo mpi cores = $PBS_NUM_PPN
echo working directory = $PBS_O_WORKDIR
echo executable = $exe
echo

pwd
ls -l $inp
ls -l $exe

export DATA=$PROJWORK/nfi011/Exnihilo/scale
export SCALE=$PROJWORK/nfi011/Exnihilo/installs/Exnihilo.20161005

aprun -n25088 -j1 -S4 $exe -i $inp
date
