from collections import namedtuple
Bedroom = namedtuple('Bedroom', 'room_num ')
Reservation = namedtuple('Reservation', 'room_num checkinDate checkoutDate lastName firstName')

def stage3():

    list_of_bedrooms =  []
    list_of_reservations = []
    reservation_dict = {}
    bb = open('stage3.txt', 'r')
    lines = bb.readlines()

    for line in lines:
        x = line.split()

        if x[0].upper() == 'PL':
            print(line[3:])
        elif x[0].upper() == 'NB':
            list_of_bedrooms.append(x[1])
        
        elif x[0].upper() == 'NR':

            if x[1] in list_of_bedrooms:
                r = Reservation(x[1], x[2], x[3], x[4], x[5])
                list_of_reservations.append(r)
                confirmation_num = 1

                for i in list_of_reservations:
                     reservation_dict[confirmation_num] = i
                     confirmation_num += 1
                     
            

                for k,v in reservation_dict.items():
                     print("reserving",v.room_num, v.checkinDate, v.checkoutDate, v.lastName, v.firstName, "confirmation #", k)
            else:
                print(x[1]  + 'cannot be reserved')

            
           
            

              
        elif x[0].upper() == 'RR':
            requested_num = x[1]
            if int(requested_num) in reservation_dict:
                reservation_dict.pop(int(requested_num))




stage3()
 

