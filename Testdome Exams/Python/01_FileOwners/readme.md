## Question
Implement a `group_by_owners() function` that:
1. Accepts a dictionary containing the file owner name for each file name.
2. Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary: 
```python 
{
'Input.txt': 'Randy', 
'Code.py': 'Stan', 
'Output.txt': 'Randy'
}
```

the `group_by_owners() function` should return 

```python
{
    'Randy': ['Input.txt', 'Output.txt'], 
    'Stan': ['Code.py']
}
```
Code : 
```python
def group_by_owners(files):
        return None

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))

```
