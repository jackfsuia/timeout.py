# timeout.py
timeout on a python function.

```python
from timeout import timeout

def func():
    return 2**(2**(10000))

if __name__ == '__main__':
    timeout_seconds = 3
    result = timeout(func, timeout_seconds)
    print("return:", result)
```
