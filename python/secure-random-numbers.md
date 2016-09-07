# Cryptographically Secure Randomness in Python

If you aren't using libsodium:
* If you need random bytes, use os.urandom().
* If you need other forms of randomness, you want an instance of random.SystemRandom() instead of just random.

```python
import sys
import random

# Random bytes
bytes = os.urandom(32)
csprng = random.SystemRandom()

# Random (probably large) integer
int = csprng.randint(0, sys.maxint)
```

[Reference](https://paragonie.com/blog/2016/05/how-generate-secure-random-numbers-in-various-programming-languages)
