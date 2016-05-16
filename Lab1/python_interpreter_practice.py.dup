Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pathlib import Path
>>> p = Path("C:\Users\sam\Downloads\Python_online_resource_files")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
KeyboardInterrupt
>>> p = Path("C:\\Users\\sam\Downloads\\Python_online_resource_files")
>>> [x for x in p.iterdir() if x.is_dir()]
[]
>>> 
>>> list(p.glob('**/*.py'))
[]
>>> p = Path("C:\\Users\\sam\Downloads")
>>> list(p.glob('**/*.py'))
[WindowsPath('C:/Users/sam/Downloads/lab1-2.py'), WindowsPath('C:/Users/sam/Downloads/lab1.py')]
>>> usr_inpt = input()
.py
>>> list(p.glob('**/*' +usr_inpt))
[WindowsPath('C:/Users/sam/Downloads/lab1-2.py'), WindowsPath('C:/Users/sam/Downloads/lab1.py')]
>>> >>> [x for x in p.iterdir() if x.is_dir()]
SyntaxError: invalid syntax
>>> [x for x in p.iterdir() if x.is_dir()]
[WindowsPath('C:/Users/sam/Downloads/inf43HW3'), WindowsPath('C:/Users/sam/Downloads/Python_online_resource_files'), WindowsPath('C:/Users/sam/Downloads/test')]
>>> user = input()
N .py
>>> a = user.split()
>>> print(a)
['N', '.py']
>>> list(p.glob('**/*' + a[-1]))
[WindowsPath('C:/Users/sam/Downloads/lab1-2.py'), WindowsPath('C:/Users/sam/Downloads/lab1.py')]
>>> import os, os.path
>>> os.walk("C:\\Users\\sam\Downloads\\Python_online_resource_files")
<generator object walk at 0x03EA68A0>
>>>  import os
 
SyntaxError: unexpected indent
>>> import os
>>> for path, dirs, files in os.walk("C:\\Users\\sam\Downloads\\Python_online_resource_files"):
	print(files)

	
['doctools.js', 'gasp_lessons.png', 'jquery.js', 'pygments.css', 'style.css', 'underscore.js']
>>> 
