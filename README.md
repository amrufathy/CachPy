# CachPy
CachPy is an object agnostic (doesn't assume anything about the objects), fast, offline caching module for python objects.

CachPy uses a naive caching mechanism. It checks if file existence only and doesn't look for input changes.

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
def func1(x, y):
    return x + y
    
print(func1(1, 2))

@cachpy(filepath='func2_file_path', ignore_cache=True)
def func2(x, y):
    return x - y
    
@cachpy(reload_cache=True)
def func3(x, y):
    return x * y
```

Parameters
* `filepath`: File path to save the object. (default = `.pickles/{module_name}__{function_name}.pickle`)
* `verbose`: Printing for debugging purposes. (default = `False`)
* `ignore_cache`: Ignore caching, doesn't read or write any files. Just calls the function to re-evaluate. (default = `False`)
* `reload_cache`: Re-evaluate the function and overwrite the saved file. (default = `False`)

*For constantly changing input values, you should set `reload_cache = True` OR `ignore_cache = True`*