from pathlib import Path

p = Path("C:\\Users\sam\Downloads")

## print every item in the list of paths and files
list_of_files = [] 
for x in p.iterdir():
    if x.is_dir():
        list_of_files.append(x)
print(list_of_files)

## listing the files based on the extension
a = list(p.glob('**/*.exe'))
print(a)
print("List of the files that has extension .exe\n\n")
for i in a:
     print(i)



## NAVIGATING INSIDE A DIRECTORIES 
q  = p/ 'Lecture7-2'
print(q.is_dir())
print(p.exists())
print(p.is_file())

print(type(p))
parts = list(p.parts)
print(parts)
print(parts[-1])

