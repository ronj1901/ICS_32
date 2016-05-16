# BandB Stage I
from collections import namedtuple
Bedroom = namedtuple('Bedroom', 'room_num')
def stage1():
    list_of_bedrooms = [] 
    bb = open ('stage1.txt', 'r')
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
stage1()
