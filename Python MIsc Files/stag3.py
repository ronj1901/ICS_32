
# BandB Stage II
from collections import namedtuple
Bedroom = namedtuple('Bedroom', 'room_num')
def stage3():

    list_of_bedrooms = [] 
    bb = open ('stage3.txt', 'r')
    lines = bb.readlines()
    #outfile = write('s', 'w') ?
    for line in lines:
        x = line.split()
        #print(x)
        if x[0].upper() == 'PL':
            print(line[3:]) 
        elif x[0].upper() == 'LB':
            print ('Number of bedrooms in service:', len(list_of_bedrooms))
            print('--------------------------------')
            for i in list_of_bedrooms:
                print(i.room_num)

        elif x[0].upper() == 'NB':
            a = Bedroom(x[1]) 
            list_of_bedrooms.append(a)
        elif x[0].upper() == 'RB':
            try:
                b = Bedroom(x[1]) 
                list_of_bedrooms.remove(b)
            except:
                print("Sorry can't delete the room",x[1] ,"; it is not in service now")
stage3()
