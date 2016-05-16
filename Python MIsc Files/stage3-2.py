
from collections import namedtuple
Bedroom = namedtuple('Bedroom', 'room_num ')
Reservation = namedtuple('Reservation', 'room_num checkinDate checkoutDate lastName firstName')
def stage3():

    list_of_bedrooms = []
    list_of_reservations = []
    reservation_dict = {}
    bb = open ('stage3.txt', 'r')
    lines = bb.readlines()
    #outfile = write('s', 'w') ?
    for line in lines:
        x = line.split()
        #print(x)
        if x[0].upper() == 'PL':
            print(line[3:])
        elif x[0].upper() == 'NB':
             
            list_of_bedrooms.append(x[1])
              
        elif x[0].upper() == 'RR':
                
                if int(x[1]) in reservation_dict:
                    reservation_dict.pop(int(x[1]))
                    #list_of_reservations.remove(reservation_dict[x[1]])
                else:
                    print("Sorry, can't cancel reservation; no confirmation number" ,x[1])
        
        elif x[0].upper() == 'NR':
            if x[1] in list_of_bedrooms:
                r = Reservation(x[1], x[2], x[3], x[4], x[5])
                list_of_reservations.append(r)
                confirmation_num = 1
                for i  in list_of_reservations:
                    reservation_dict[confirmation_num] = i
                    confirmation_num += 1
                print("Reserving room", x[1], "for", x[4], x[5], "-- Confirmation #", confirmation_num - 1)
                print("\t(arriving", x[2], ", departing", x[3], ")")
            else:
                print("Sorry; can't reserve room", x[1],"; room not in service")

        elif x[0].upper() == 'LR':
            print ('Number of reservations:', len(list_of_reservations))
            print('No. Rm. Arrive      Depart     Guest')
            print('------------------------------------------------')
            confirmation = 0
            for k,v in reservation_dict.items():
                
                #print("Reserving ", v.room_num, "arriving from ", v.checkinDate,"departing ", v.checkoutDate, "in the name of ", v.lastName, v.firstName, "confirmation #", k)
                print("{:3d} {:3s} {:10s} {:10s} {:15s}".format(k,v.room_num,v.checkinDate, v.checkoutDate, v.lastName  +" " + v.firstName))

        
stage3()
