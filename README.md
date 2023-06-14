
Initialize  DVC 

```
dvc init
```

## DVC Cache

The DVC cache is a hidden storage for files and directories tracked by DVC, and their different versions. 
we configured the project's cache in a location shared by other projects to avoid that multiple users have copies of the same project on a single machine. 

Create shared cache

```
dvc cache dir /home/aime/dvc-cache 
dvc config cache.shared group
dvc config cache.type symlink
```

DVC remotes provide access to external storage locations to track and share your data and ML models. 
It does backup different versions of datasets and models. 

Setting up a remote storage 
```
dvc remote add -d remote /home/aime/backup
```
