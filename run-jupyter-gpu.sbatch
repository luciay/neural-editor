#!/bin/bash

#SBATCH --job-name=jupyterGPU
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=50GB
#SBATCH --time=30:00:00
#SBATCH --gres=gpu:1

module purge
module load cuda
module load cudnn
module load python/intel/2.7.12

jupyter_dir=/home/$USER/
cd $jupyter_dir

port=$(shuf -i 6000-9999 -n 1)

/usr/bin/ssh -N -f -R $port:localhost:$port log-0
/usr/bin/ssh -N -f -R $port:localhost:$port log-1

cat<<EOF

Jupyter server is running on: $(hostname)
Job starts at: $(date)

Step 1 :

If you are working in NYU campus, please open an iTerm window, run command

ssh -L $port:localhost:$port $USER@prince.hpc.nyu.edu

If you are working off campus, you should already have ssh tunneling setup through HPC bastion host, 
that you can directly login to prince with command

ssh $USER@prince

Please open an iTerm window, run command

ssh -L $port:localhost:$port $USER@prince

Step 2:

Keep the iTerm windows in the previouse step open. Now open browser, find the line with

The Jupyter Notebook is running at:

the URL is something: http://localhost:${port}/?token=XXXXXXXX

you should be able to connect to jupyter notebook running remotly on prince compute node with above url

EOF

unset XDG_RUNTIME_DIR
if [ "$SLURM_JOBTMP" != "" ]; then
    export XDG_RUNTIME_DIR=$SLURM_JOBTMP
fi

HOME=/home/$USER
DATA_DIR=$HOME/neural-editor-data
REPO_DIR=$HOME/neural-editor
SINGULARITY_PATH=/share/apps/singularity/2.5.1/bin/singularity
TEXTMORPH_IMG=/beegfs/work/public/singularity/textmorph-1.2.img

export TEXTMORPH_DATA=$DATA_DIR
export PYTHONPATH=.:$REPO_DIR:$PYTHONPATH

$SINGULARITY_PATH exec --nv $TEXTMORPH_IMG jupyter notebook --no-browser --port $port
