
# Shambhu Thapa  10677794  Abigail Jimenez 18405220



from pathlib import Path
import shutil

def searchFile(path:Path)->list:
    '''
    recursively traverse through the directories
    and subdirectoriess to search for files until found
    '''
    list_file = []
    for sub_dir in path.iterdir():
        if sub_dir.is_file():
            list_file.append(sub_dir)
        elif sub_dir.is_dir():
            list_file.extend(searchFile(sub_dir))

    return list_file

def operation()-> None:
    conntinue = False
    while conntinue == False:
        
        a = (input().strip())
        path = Path(a)
        conntinue = path.exists()
        if conntinue == False:
            print("ERROR")
    
    conntinue = False
    while conntinue == False:       
        user_input2 = input()
        second_line = user_input2.split()
        fileName = second_line[-1]
        results = []
      
        if second_line[0] == 'N':    
            for dirr in searchFile(path):  
                if Path(dirr).match(fileName):
                    results.append(str(dirr))
                else:
                    continue
            break
            
        elif second_line[0] ==  'E' and len(second_line[-1]) > 0:
            file_exten = second_line[-1].strip('.').strip()
            file_exten = '.' + file_exten
            for item in searchFile(path):
                if (Path(item).suffix == file_exten):
                    results.append(str(item))
                else:
                    continue
            break

        elif (second_line[0] == 'S'  and second_line[-1].isdigit):
            fileSize =(second_line[-1])
            filesize =int(fileSize)
            for item in searchFile(path):
                if ((Path(item).stat().st_size > filesize)):
                    results.append(str(item))
                else:
                    continue
            break
        else:
            print("ERROR")
            
    conntinue = True
    while conntinue == True:
        user_input3 = input()
        if user_input3 == 'P':
            if len(results) > 0:
                for item in results:
                    print(item)
            else:
                print("there are non such files of that name")
            break
        elif user_input3 == 'F':
            if len(results) >0:
                for i in results:
                    
                        
                    try:
                        
                        f = open(i, 'r')
                        print(i)
                        data = f.readlines()
                        print(data[0])
                        
                    except:
                        
                        print("This is not a valid file")
            else:
                print(" No such File found in the directory")
                    
            break

        elif user_input3 == 'D':
            for i in results:
                shutil.copy2(i, i + ".dup")
            break
        elif user_input3 == 'T':
            for i in results:
                Path(i).touch()
        elif user_input3 != 'P' or 'F' or 'D' or'T':
            print("ERROR")


if __name__ == '__main__':
    ''' only runs when the module is run '''

    operation()

