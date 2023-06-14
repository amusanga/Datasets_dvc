1. To generate the dataset metadata

```
python ttiff_images_dataset/prepare.py 
```

2. Added data to dvc

```
dvc add ttiff_images_dataset/data
```
```
git add ttiff_images_dataset/data.dvc ttiff_images_dataset/.gitignore 
```
3. commit data and tag data
```
git commit -m "Added ttiff images dataset."
```

```
 git tag -a "Ttiff_dataset_v1.0" -m "Added Ttiff dataset" 
```

4. push data to source of truth
```
dvc push
```
```
dvc status
```


Making changes by More data inside

repeat 1

dvc status 

```python
ttiff_images_dataset/data.dvc:                                                                    
        changed outs:
                modified:           ttiff_images_dataset/data
```

repeat 2

```
git commit -m "Added More Tiff images dataset"  
git tag -a "Ttiff_dataset_v2.0" -m "Added more  Ttiff dataset"
```

repeat 4

### Switching between workspace versions
The DVC command that helps get a specific committed version of data is designed to be similar to git checkout. All we need to do in our case is to additionally run dvc checkout to get the right data into the workspace.

```
git checkout Ttiff_dataset_v1.0
dvc checkout
```

### Using our versioned data in our project with Python API

#### Load dataset version 1
```
with dvc.api.open(
    'ttiff_images_dataset/data/metadata.csv',
    repo='/home/aime/TrustStamp/Datasets_dvc',
    remote="remote",
    mode='rb',
    rev='Ttiff_dataset_v1.0'
) as f:
    
    Ttiff_dataset_v1 = pd.read_csv(f)

```
#### Load dataset version 2
```
with dvc.api.open(
    'ttiff_images_dataset/data/metadata.csv',
    repo='/home/aime/TrustStamp/Datasets_dvc',
    remote="remote",
    mode='rb',
    rev='Ttiff_dataset_v2.0'
) as f:
    
    Ttiff_dataset_v2 = pd.read_csv(f)

```

Pull the data in another project

```
dvc import --rev "Ttiff_dataset_v1.0" ~/TrustStamp/Datasets_dvc ttiff_images_dataset/data/tiff_images
```
