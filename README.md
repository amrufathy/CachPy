# CachPy
CachPy is an object agnostic (doesn't assume anything about the objects), fast, offline caching module for python objects.

## Installation
```
pip install setup.py
```

## Compatability
CachPy is compatible with Python 2.7.x and 3.

## Usage
```python
from cachpy import cachpy


@cachpy()
def my_function(x, y):
    return x + y
    
print(my_function(1, 2))
```

Parameters
* `filepath`: File path to save the object.
* `verbose`: Printing for debugging purposes.
* `ignore_cache`: Ignore caching, doesn't read or write any files. Just calls the function to re-evaluate.
* `reload_cache`: Re-evaluate the function and overwrite the saved file.