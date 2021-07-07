# qzv-viewer

This is a simple package allowing you to view QIIME2 visualisers (files ending with `.qzv`) in notebooks. Currently, only Jupyter notebook viewer is displayed correctly. 

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

# Demo

To run the demo clone into the repository:

```
git clone https://github.com/adamovanja/qzv-viewer.git
```

and open the notebook in `qzv-viewer/qzv-viewer/src/tests/demo_jupyter.ipynb` with jupyter notebook.
