from pathlib import Path
import os

conntinue = False
while conntinue == False:
    user_input = input()
    p = Path(user_input)
    conntinue = p.exists()
    if conntinue == False:
        print("ERROR")
        
##Second line

conntinue = False
while conntinue == False:       
    user_input2 = input()
    second_line = user_input2.split()
   ## print(user_input2)
    q = Path(user_input2)
    results = []
        
    if second_line[0] == 'N':
        #file_path = Path(user_input + user_input2[1])
        fileName = second_line[-1]
        for path, dirs, files in os.walk(user_input):
            results.extend(files)
        if fileName in files:
            print(fileName)
            

        break
    elif second_line[0] ==  'E':
        ###a = list(p.glob('**/*' + second_line[-1]))
        
        for path, dirs, files in os.walk(user_input):
            for i in files:
                if second_line[-1] in i:
                    results.append(i)
                else:
                    continue
        break
                        

    elif second_line[0] ==  'S':
        file_size = int(second_line[-1])
        for path, dirs, files in os.walk(user_input):
            for file in files:
                if os.path.getsize(file) > file_size:
                    results.append(file)
                else:
                    continue
        break
    elif second_line[0] != 'N' or 'E' or 'S':
        print("ERROR")

import shutil

conntinue = True
while conntinue == True:
    user_input3 = input()        
    ## C:\Users\shambhut\Desktop\ICS32\Lab1
    if user_input3 == 'P':
        for item in results:
            print(item)
        break
    elif user_input3 == 'F':
        for i in results:
            f = open(i, 'r')
            data = f.readlines()
            print(data[0])
        break

    elif user_input3 == 'D':
        for i in results:
            shutil.copy2(i, i + ".dup")
        break
    elif user_input3 != 'P' or 'F' or 'D':
        print("ERROR")



    
            
     


        
        



