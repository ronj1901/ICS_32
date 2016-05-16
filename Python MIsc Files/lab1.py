__author__ = 'sam'


## lets make a function to get the input

from pathlib import Path
##def get_first_input(user-inout):
##    user_input = input()
##
##    if p.is_dir() == False:
##        print("ERROR")
##        get_input()
##
##    else:
##        print("valid input taken")
##        print(p)
##
##
##get_first_input = def get_second_input()
##

##conntinue = False
##while conntinue == False:
##    user_input = input()
##    p = Path(user_input)
##    conntinue = p.exists()
##    list_of_files = []
##    if conntinue == False:
##        print("ERROR")
##    if conntinue == True:
##
##        for x in p.iterdir():
##
##            if x.is_dir():
##
##                for sub in x.iterdir():
##
##                    list_of_files.append(sub)
##
##
##    ##print(list_of_files)
##    for files in list_of_files:
##        print(files)
##
#### testing the user input
##
##conntinue = False
##while conntinue == False:
##    user_input2 = input().split
##    q= user_input2
##    new_dir_to_search = p/Path(q[-1])
##    print(new_dir_to_search.is_file())
##
##    for item in list_of_files:
##        if item = new_dir_to_search:
##            print(item)
##        else:
##
##


##def finddir():
##    conntinue = False
##    user_input = input()
##    while conntinue == False:
##        p = Path(user_input)
##        conntinue = p.exists()
##        if conntinue == False:
##            print("ERROR")
##        if conntinue == True:
##            search_file = input("Enter a file name: ")
##        user_input = input()
##
##
##
##
##
##finddir()
##
##
##
##  /Users/sam/Desktop/ICS 32

def searchFile(path:Path)->list:
    ''' recursively search for files until found'''
    list_file = []
    for sub_dir in path.iterdir():
        if sub_dir.is_file():
            list_file.append(sub_dir)
        elif sub_dir.is_dir():
            list_file.extend(searchFile(sub_dir))


    return list_file
    #print(path)



if __name__ == '__main__':
    conntinue = False
    while conntinue == False:
        path = Path(input())
        #p = Path(user_input)
        conntinue = path.exists()
        if conntinue == False:
            print("ERROR")
        print(path)


    conntinue = False
    while conntinue == False:
        user_input2 = input()
        second_line = user_input2.split()
       ## print(user_input2)

        results = []

        fileName = second_line[-1]   ## filename to be searched for 2nd input

        if second_line[0] == 'N':
            print(searchFile(path))














