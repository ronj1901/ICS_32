
def count_string(All: [[]])->int:
    nlist = []
    for  x in All:
        if type(x) == str:
            nlist.append(x)
        elif type(x) == list:
            nlist.append(count_string(x))
        else:
            continue
            
            
    return len(nlist)


print(count_string(["sham" , "thapa", "goes"]))

