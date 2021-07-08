# qzv-viewer

This is a simple package allowing you to view QIIME2 visualisers (files ending with `.qzv`) in notebooks. Currently, only Jupyter notebook viewer allows you to view all types of QIIME2 visualisers correctly. In the VSCode notebook viewer only non-emperor plots are supported with an additional clean-up step required after the plot.

# Install
We recommend using the functonalities in a conda environment with the required dependencies installed within:
```
conda create -y -n qzv-viewer
conda activate qzv-viewer

conda install \
  -y -c conda-forge -c bioconda -c qiime2 -c defaults \
  qiime2 q2cli xmltodict jupyter
```
Now install qzv-viewer within:
```
pip install git+https://github.com/adamovanja/qzv-viewer.git
```

# Jupyter Notebook Demo

To run the demo in jupyter notebook, clone into the repository:

```
git clone https://github.com/adamovanja/qzv-viewer.git
```

and open the demo notebook:
```
cd qzv-viewer/src/tests/
jupyter notebook demo_jupyter.ipynb

```

# VSCode Notebook Demo

To run the demo in VSCode, clone into the repository:

```
git clone https://github.com/adamovanja/qzv-viewer.git
```

and open the demo notebook:
```
cd qzv-viewer/src/tests/
jupyter notebook demo_vscode.ipynb
```

As you can see there is currently an additional clean-up step required in VSCode after viewing the visualisations.


# Contact

In case of questions or comments feel free to raise an issue in this repository.
