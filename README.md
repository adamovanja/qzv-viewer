# display-qzv

This is a simple package allowing you to view QIIME2 visualisers(files ending with `.qzv`) in notebooks. Currently, only Jupyter notebook viewer is displayed correctly. 

# Install
We recommend using the functonalities in a conda environment with the required dependencies installed within:
```
conda create -y -n display
conda activate display

conda install \
  -c conda-forge -c bioconda -c qiime2 -c defaults \
  qiime2 q2cli xmltodict
```
Now install display-qzv within:
```
pip install 
```

