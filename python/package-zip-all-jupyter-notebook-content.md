# Download all files in a path on Jupyter notebook server
Try running this is as separate cell in one of your notebooks:

```
!tar cvfz notebook.tar.gz *
```

If you want to cover more folders up the tree, write `../` before the `*` for every step up the directory. The file `notebook.tar.gz` will be saved in the same folder as your notebook.
