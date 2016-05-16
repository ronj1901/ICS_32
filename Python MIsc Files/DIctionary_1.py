# DICTIONARY

tel = {'jack': 4098, 'sape':4139}
tel['guido'] = 4127
print(tel)
print(sorted(tel))



print("list:", list(tel))

print('jack' in tel)


def return_dict(x:int)->dict:
    
    return {x: x**2 for x in (2, 4, 6)}


print(return_dict(2))


for k,v in tel.items():
    print(k,v)


for i in reversed(range(1, 10, 2)):
    print(i)



#SET 
print("let us make my name into set")

my_name = "shambhu"
shambhu = set(my_name)
his_name = "Swargabami"
ss=  set(his_name)
print("my_name , ", shambhu)
print("his_name, ", ss)

print("intersection of our name: ",shambhu.intersection(ss))
print("union of our name ",shambhu.union(ss))
print(shambhu.difference(ss))

# STRING FORMATTING

name =  "Shambhu Thapa"
ID = 1067774
classes =  "ICS31"
total_units = 4 


print("{:15s} {:8d} {:7s} {:3d}".format(name, ID, classes, total_units))

name_list  =[]
ID_list = []
class_list = []
unit_list = []

for i in range(2):
    a = input("what is the name of strudent? :  " )
    name_list.append(a)
    b = int(input("what is the  ID of student? :  ", ))
    ID_list.append(b)
    c= input("what class is student? :  " ,)
    class_list.append(c)
    d = int(input("what unit: "))
    unit_list.append(d)

for i in name_list:
    for j in ID_list:
        for k in class_list:
            for l in unit_list:
                
print("{:s} {:8d} {:s} {:3d}".format(i, j, k, l))
                


list1 = [1,3,6,78,8]
print(list1[-1])
list1 = ['a', 'b', 'c', 'd']
print(list1[1:-1])





