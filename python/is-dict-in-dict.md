# How to check if one dict contained in other dict?
Is there a simple way to test if the first dict is part of the second dict, with all its keys and values?

```python
Method                                                      Time [s]
first.viewitems() <=second.viewitems()                           0.9
set(first.items()).issubset(second.items())                      7.3
len(set(first.items()) & set(second.items())) == len(first)      8.5
all(first[key] == second.get(key, sentinel) for key in first)    6.0
```
