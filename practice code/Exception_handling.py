Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> import math
>>> math.sqrt(-1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    math.sqrt(-1)
ValueError: math domain error
>>> try
SyntaxError: invalid syntax
>>> try:
	math.sqrt(-1)
except ValueError:
	print("operation could not be completed because there is no such number that results -ve when squared")
else:
	print("success! ")
finally:
	print("sigh ! "  )

	
operation could not be completed because there is no such number that results -ve when squared
sigh ! 
>>> try:
	result.append(3)
except
SyntaxError: invalid syntax
>>> try:
	result.append("2)
		      
SyntaxError: EOL while scanning string literal
>>> cleart
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    cleart
NameError: name 'cleart' is not defined
>>> clr
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> clear()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> f = open("randomfile.txt ")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    f = open("randomfile.txt ")
FileNotFoundError: [Errno 2] No such file or directory: 'randomfile.txt '
\ 
>>> try:
	f =  open("randomfile.txt", 'r')
except:
	print("no such file found" )
else:
	print("hurray, there is no error and the program ran as expected")
finally:
	print(" no matter what you get as result i will print this statement.")

	
no such file found
 no matter what you get as result i will print this statement.
>>> no matter what you get as result i will print this statement.
SyntaxError: invalid syntax
>>> f = open("Desktop\\test.txt", "r")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f = open("Desktop\\test.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'Desktop\\test.txt'
>>> FileNotFoundError: [Errno 2] No such file or directory: 'Desktop\\test.txt'
SyntaxError: invalid syntax
>>> 
>>> f = open("/Users/sam/Desktop/test.txt", "r")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    f = open("/Users/sam/Desktop/test.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: '/Users/sam/Desktop/test.txt'
>>> 
>>> f = open("/Users/sam/Desktop/test.txt", "r")
>>> f.read(2)
'my'
>>> f.read(3)
' na'
>>> f.realines()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    f.realines()
AttributeError: '_io.TextIOWrapper' object has no attribute 'realines'
>>> f.readlines()
['me is shambhu thapa \n', 'I live in Los Angeles \n', 'I go to UCI \n', '\n']
>>> f.tell()
63
>>> f.seek(0)
0
>>> f.readline()
'my name is shambhu thapa \n'
>>> f.seek(0)
0
>>> f.read(12)
'my name is s'
>>> f.seek(12)
12
>>> f.seek("name")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    f.seek("name")
TypeError: unorderable types: str() < int()
>>> f.seek(62)
62
>>> f.readlline()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    f.readlline()
AttributeError: '_io.TextIOWrapper' object has no attribute 'readlline'
>>> f.readline()
'\n'
>>> import OS
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    import OS
ImportError: No module named 'OS'
>>> import os
>>> os.remove("/Users/sam/Desktop/test.txt")
>>> 
>>> 
>>> L = [1,2,3,4,5,45]
>>> L[6]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    L[6]
IndexError: list index out of range
>>> try:
	print(L[6])
except IndexError:
	print("ouch ")
else:
	print("success")
finallyL
SyntaxError: invalid syntax
>>> try:
	print(L[6])
except IndexError:
	print("ouch ")
else:
	print("success")

	
ouch 
>>> try:
	print(L[6])
except IndexError as e:
	print("ouch ")
else:
	print("success")

	
ouch 
>>> try:
	print(L[6])
except IndexError as e:
	print("ouch ")
else:
	print(e)

	
ouch 
>>> try:
	print(L[6])
except IndexError as e:
	print("ouch ")
else:
	print(str(e))

	
ouch 
>>> 
>>> try:
	print(L[6])
except IndexError,e:
	print("ouch ")
else:
	print(str(e))

SyntaxError: invalid syntax
>>> try:
	print(L[6])
except Exception IndexError,e:
	print("ouch ")
else:
	print(str(e))
	
SyntaxError: invalid syntax
>>> try:
	print(L[6])
except IndexError as e:
	print("ouch,", str(e) )

	
ouch, list index out of range
>>> ICS 
