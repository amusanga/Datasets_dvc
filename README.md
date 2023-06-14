
Initialize  DVC 

```
dvc init
```

Create shared cache

```
dvc cache dir /home/aime/dvc-cache 
dvc config cache.shared group
dvc config cache.type symlink
```
Setting up a remote storage 
```
dvc remote add -d remote /home/aime/backup
```
