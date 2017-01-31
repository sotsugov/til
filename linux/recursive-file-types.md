# Recursive statistics on file types in directory
Command explanation

```
$ find . -type f | sed 's/.*\.//' | sort | uniq -c
```

* `find` recursively prints all filenames
* `sed` deletes from every filename the prefix until the file extension
* `uniq` assumes sorted input `-c` does the counting (like a histogram).

