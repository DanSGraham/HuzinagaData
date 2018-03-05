# .bashrc startup script for login shells
#

# Set your umask.
umask 077       # -- private, only you have access to your files
# umask 022     # -- anyone can read and execute your files
# umask 027     # -- only members of your group can read/execute your files

# Set the prompt.
PS1="\u@\h [\w] % "

# Add your aliases here.
# alias s='ssh -X'

# Set your environment variables here.
# export VISU'AL=vim
export PYTHONPATH=$PYTHONPATH:~/code/python/scripts
export PYTHONPATH=$PYTHONPATH:~/code/python/pyscf
export PYTHONPATH=$PYTHONPATH:~/code/python/pyberny
export PYTHONPATH=$PYTHONPATH:~/code/python/rmsd
export PYTHONPATH=$PYTHONPATH:~/code/python/mpi4pyscf

#Set path here.
export PATH=$PATH:~/scripts

# Uncomment the if statement below to enable bash completion.
# if [ -f /etc/bash_completion ]; then
#  source /etc/bash_completion
# fi

# Load modules here
module load python
module load gaussian/g16.a03

# Startup behavior
#cd ~/python_modules/pyscf
#git pull
#cd
shopt -s checkwinsize

GRTNG1="Hello, Daniel. Current jobs running:"
GRTNG2=""
#echo $GRTNG1
#qstat -a
#echo $GRTNG2
