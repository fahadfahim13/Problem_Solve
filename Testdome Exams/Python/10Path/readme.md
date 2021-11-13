## Question
Write a function that provides `change directory (cd) function` for an abstract file system.
<br />
Notes:
* Root path is '/'.
* Path separator is '/'.
* Parent directory is addressable as '..'.
* Directory names consist only of English alphabet letters (A-Z and a-z).
* The function should support both relative and absolute paths.
* The function will not be passed any invalid paths.
* Do not use built-in path-related functions.
For example:
```python
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
```
should display **'/a/b/c/x'**.
Code: 
```python
class Path:
    def __init__(self, path):
        self.current_path = path
    def cd(self, new_path):
        pass
path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
```