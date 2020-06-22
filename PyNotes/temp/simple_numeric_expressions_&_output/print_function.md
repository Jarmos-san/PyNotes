`print()` function
-----

- The `print()` function prints the given object to the standard ouput device i.e the screen or a text stream file. Put more briefly, Python does two things:
    + Converts the object into strings and
    + puts the chraracter on the standard output.

- The syntax of the `print()` function is as follows:
    
    `print(*objects, sep=' ', end='\n', file=sys.stdout)`

- `print()` parameters:
     + ***objects** - object to be printed to standard ouput where * stands for multiple objects.
     + **sep** - By default passes a white space used to seperate objects.
     + **end** - By default passes a new line.
     + **file** - by default passes `sys.stdout` but can be changed using the `write()` method to print an object to a file.

_**Example:**_

```Python
#Print Multiline Output
print("335/113=", end=" ")
print(335.0/113.0)
print("Hi, Mom", "Isn't it lovely?", end=" ")
print('I said,"Hi".', 42, 91056)
```
_**Output:**_

```
335/113= 2.9646017699115044
Hi, Mom, Isn't it lovely? I said, "Hi". 42 91056
```

- The `print()` function can also write an object to a file using the `file` parameter like,

```Python
sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()
```
The above script shows Python trying to open a file, `python,txt` in writing mode which is then passed to the `sourceFile` variable object. After that Python tries to write the the string `'Pretty cool, huh!` into the file using the `file` parameter before closing the file with the `sourceFile.close() function. 

_**Note:**_

- The `print` statement is replaced by the `print()` function from Python3 onwards.
- `sep` and `end` are keywords in Python thus it's important to pass the variables into the parameters specifically rather than just without the parameters. Like so....

```Python
#This is wrong!!
print(*objects, "|", ","")

#This is the right way to do it!!
print(*objects, sep="|", end=',')
```
- Although the `print()` function doesn't return any value other than `None`

_**References:**_
- [Building Skills in Python](http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf#section.5.1)
- [Programiz](https://www.programiz.com/python-programming/methods/built-in/print)
- [Print Function, Part I -- Hands on Python tutorial](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/print1.html)
- [Thomas Coehlar - Python Notes](http://thomas-cokelaer.info/tutorials/python/print.html)