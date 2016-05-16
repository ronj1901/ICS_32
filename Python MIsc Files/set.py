###SET


s = {1, 2, 3, 4, 5}
d = {'a':1, 'b':2, 'c':3}
empty_dict = { }
empty_set = set()
t = set([2,4,6,8,10])

L = [1,3,2,5,4,2,4,1,3,4,1,5,2,4,2,3,4,2,3,6,5,2,1,2,2,2,2,2,2]

uniqueL = set(L)
print(list(uniqueL))

print('Unique elements in L: ', list(set(L)))


print("Union of s and t:", s | t)
print("Intersection of s and t:", s & t)
print("Subtraction of t from s:", s - t)
print("Symmetric differens of s and t:", s ^ t)
