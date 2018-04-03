# Evaluation of Neural editor
We use NYU's HPC Prince cluster.

1. Set up Neural Editor on Prince by following the original instructions below these steps.

2. In Prince cluster, set your net ID in the following #SBATCH directives:
```
#SBATCH --mail-user=NETID@nyu.edu
```
Set your net ID for your home directory:
```
HOME=/home/NETID
```
Then run: 
```
sbatch billion.s
sbatch yelp.s
```
This will output two files: slurm_onebil.out and slurm_yelp.out.

3. Download the two output files and graph_slurm.py onto your local machine. 

4. Run python file graph_slurm.py to generate graphs of training metrics.


# Neural editor

Source code accompanying our paper [Generating Sentences by Editing Prototypes](https://arxiv.org/abs/1709.08878).

**Authors:** Kelvin Guu\*, Tatsunori B. Hashimoto\*, Yonatan Oren, Percy Liang
(\* equal contribution)

- We are drafting a more detailed README in the
  [README](https://github.com/kelvinguu/neural-editor/tree/readme) branch (see here for dataset links)
- This is research code meant to serve as a reference implementation. We do not
  recommend heavily extending or modifying this codebase for other purposes.

If you have questions, please email Kelvin at `guu.kelvin` at `gmail.com`.
