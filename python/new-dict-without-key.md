# Create a new dict from old without having some keys included

```python
definition = {k: definition[k] for k in definition.keys() if 'op:' not in k.lower()}
```
