# Neural Editor Sentence Completion
We use NYU's HPC Prince cluster.

1. Set up Neural Editor's `neural-editor` and `neural-editor-data` folders on Prince by following the original Neural Editor instructions below:
> ## Neural editor
>
> Source code accompanying our paper [Generating Sentences by Editing Prototypes](https://arxiv.org/abs/1709.08878).
>
> **Authors:** Kelvin Guu\*, Tatsunori B. Hashimoto\*, Yonatan Oren, Percy Liang
> (\* equal contribution)
>
> - We are drafting a more detailed README in the [README](https://github.com/kelvinguu/neural-editor/tree/readme) branch (see here for dataset links)
> - This is research code meant to serve as a reference implementation. We do not recommend heavily extending or modifying this codebase for other purposes.
>
> If you have questions, please email Kelvin at `guu.kelvin` at `gmail.com`.



2. To begin a training run on NYU's Prince cluster for the following datasets:
- Google's Billion Words Dataset = 'billion'
- Yelp Reviews Dataset = 'yelp'
- Penn's Tree Bank = 'ptb'
- Bach Music\* = 'bach'

```
sbatch <dataset>.s
```
For example, to run the neural editor sentence completion on the ptb dataset submit: `sbatch ptb.s` to Prince.

The `sbatch` scripts run a Singularity image of Kelvin Guu's Docker image (kelvinguu/textmorph:1.2), located on Prince's shared folders. The training run will output a slurm file: `slurm_<dataset>.out`.

\*all music dataset `sbatch` scripts are located in `composer_scripts` folder


**Notes**:
- `sbatch` scripts should exist on the same directory level as `neural-editor`
- `neural-editor-data` from Step 1 should be saved to `/scratch/$USER/` for sufficient storage
- `midi_split` folder should be in `~/neural-editor-data`
- contents inside of this repo's `word_vectors` folder should be added to existing contents of `~/neural-editor-data/word_vectors`


3. After training has completed, to generate a demo in Jupyer Notebook submit to Prince:
```
sbatch run-jupyer-gpu.sbatch
```
and follow the directions. Once in `neural-editor-completion.ipynb` notebook, set `EDIT_RUN` to the desired edit run checkpoint number located in `~/neural-editor-data/edit_runs`.

