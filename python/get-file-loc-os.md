
Get current file location OS-agnostic

```bash
$ pwd
/Users/igor/Dropbox/Backup/Dev
```

```python
>>> import os
>>> import inspect
>>> file_path = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
>>> print file_path
/Users/igor/Dropbox/Backup/Dev
>>>
```

```python
>>> os.getcwd()
'/Users/igor/Dropbox/Backup/Dev'
```

```python
os.path.dirname(os.path.realpath(__file__))
```
