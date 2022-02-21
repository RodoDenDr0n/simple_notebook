# simple_notebook
## About the project
This project represents a simple notebook that can be used to note things in it and search for needed information
## Fuctions used in the project
```python
main()
```
## Classes used in the project
```python
class Notebook
class Note
class Menu
class CommandOption
```
## About functions
### main()
The ```main()``` function is responsible for creating the notebook and running the program
```python
def main():
    notebook = Notebook(notes=[])
    while True:
        Menu().menu(notebook)
```
```while True``` cycle is used to call the menu method from Menu
## About classes
### Notebook()
Class Notebook is witten to represent the Notebook object and has such methods as: 
- ```__init__(self, notes)``` which is responsible for creating class Notebook
- ```search(self, filter)``` which is responsible for searchin info in notebook
- ```new_note(self, memo, tags="")``` which is responsible for creating new note
- ```modify_memo(self, note_id, memo)``` which is responsible for modifying memo
- ```modify_tags(self, note_id, tags)``` which is responsible for modifying tags
### Note()
Class Note is witten to represent the Note object and has such methods as:
- ```__init__(self, memo, creation_date, tags)``` which is responsible for creating class Note
- ```match(self, search_filter)``` which is responsible for checking searched phrase matches note memo or tags, if match is found returns True, else False class
### Menu()
Class Menu is witten to represent the Menu object. This function has the static method that is responsible for navigating the menu and getting user's commands
```python
@staticmethod
    def menu(notebook):
        user_command = input(...
        if user_command == "...
            return CommandOption. ...
        elif ...
        ...    
```
There a number of commands available for user to enter:
- change_memo
- modify_tags
- new_note
- search
- show_notes
Those commands are realised in CommandOption class
### CommandOption()
Class CommandOption is witten to represent the CommandOption object and has a number of static methods
- ```get_note_id(notebook)```
- ```get_memo(new=False)```
- ```get_tags(new=False)```
- ```get_search_phrase()```
- ```show_search_results(matches)```
- ```change_memo(notebook)```
- ```modify_tags(notebook)```
- ```new_note(notebook)```
- ```search(notebook)```
And one dynamic method
- ```__str__(self)```








