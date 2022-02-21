# simple_notebook
## About the project
This project represents a simple notebook that can be used to note things in it and search for needed information
## Classes used in the project
```python
class Notebook
class Note
class Menu
class CommandOption
```
## Fuctions used in the project
```python
main()
```
## About functions
The ```main()``` function is responsible for creating the notebook and running the program
```python
def main():
    notebook = Notebook(notes=[])
    while True:
        Menu().menu(notebook)
```
```while True``` cycle is used to recursively call the function and 
