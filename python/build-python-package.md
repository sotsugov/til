# Developing Python Packages

* Creating folder structure
```
helloworld/
    helloworld/
        __init__.py
    setup.py
```

* Contents `__init__.py`
```
def helloworld():
    return 'Hello world'
```

* Contents `setup.py`
```
from setuptools import setup, find_packages
setup(
    name='helloworld',
    version='0.0.1',
    description='A hello world package',
    url='https://github.com/...',
    author='Igor Sotsugov',
    author_email='reveous@gmail.com',
    packages=find_packages(exclude=('tests')),
)
```

* Building the package
```
$ python setup.py sdist bdist_wheel
...
$ ls dist/
helloworld-0.0.1-py2-none-any.whl
helloworld-0.0.1.tar.gz
```

* Installing the package
```
$ pip install dist/helloworld-0.0.1.tar.gz
...
$ python
Python 2.7.12 (default, Jul  1 2016, 15:12:24)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import helloworld
>>> helloworld.helloworld()
'Hello world'
```
