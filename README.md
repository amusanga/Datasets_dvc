1. To generate the dataset metadata

```
python crop_images_dataset/prepare.py 
```

2. Added data to dvc

```
dvc add crop_images_dataset/data/metadata.csv 
```
```
git add crop_images_dataset/data/metadata.csv.dvc  
```
3. commit data and tag data
```
git commit -m "Added Cropped images dataset"
```

```
git tag -a "CropsDataset_v1.0" -m "orignal crops dataset" 
```

4. push data to source of truth
```
dvc push
```
```
dvc status
```


Making changes by replicating some data inside

repeat 1

dvc status 

```python
crop_images_dataset/data/metadata.csv.dvc:                            
        changed outs:
                modified:           crop_images_dataset/data/metadata.csv
```

repeat 2

```
git commit -m "Added More Crops images dataset"  
git tag -a "CropsDataset_v2.0" -m "Added more crops dataset"
```

repeat 4

