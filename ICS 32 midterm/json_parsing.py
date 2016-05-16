Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/sam/Desktop/ICS 32 midterm/urllib.py ============
>>> import urllib.parse
>>> urllib.parse.urlencode([('name','Shambhu'),('age', 23), ('school','UCI')])
'name=Shambhu&age=23&school=UCI'
>>> # parsing the json response
>>> import json
>>> x = '{"name": "Shambhu", "age":23, "qualities":["intellegent","smart", "cute","brave", "perfect"]}'
>>> obj = json.loads(x)
>>> obj['name']
'Shambhu'
>>> obj[age]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    obj[age]
NameError: name 'age' is not defined
>>> obj["qualities"]
['intellegent', 'smart', 'cute', 'brave', 'perfect']
>>> for quality in obj[qualities]
SyntaxError: invalid syntax
>>> for quality in obj[qualities]:
	print(quality)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for quality in obj[qualities]:
NameError: name 'qualities' is not defined
>>> for quality in obj["qualities"]:
	print(quality)

	
intellegent
smart
cute
brave
perfect
>>> 
