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
