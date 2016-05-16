#### MY solution  to  stage IV

from collections import namedtuple
Bedroom = namedtuple('Bedroom', 'room_num ')
Reservation = namedtuple('Reservation', 'room_num checkinDate checkoutDate lastName firstName')

def stage4():

    list_of_bedrooms = []
    list_of_reservations = []
    reservation_dict = {}

    cc = open("stage4.txt", "r")
    lines = cc.readlines()
    for line in lines:
        x = line.split()

        if x[0].upper()  == 'PL':
            print(line[3:])
        elif x[0].upper == 'NB':  # add rooms to the list
            list_of_bedrooms.append(x[1])
        elif x[0].upper() == 'RR': ## removing reservation . canceling
            if int(x[1]) in reservation_dict:
                reservation_dict.pop(int(x[1]))
            elif int(x[1]) not in reservation_dict:           
                print("Sorry, can't cancel reservation; no confirmation number" ,x[1])

        
        elif x[0].upper() == 'NR':
            if x[1] in list_of_bedrooms:
                checkin_num = x[2].split("/")
                checkout_num = x[3].split("/")
                canPrint = False
                if checkout_num[2] > checkin_num[2]:
                    canPrint = True
                elif checkout_num[2] == checkin_num[2]:
                    if checkout_num[0] == checkin_num[0]:
                        if checkout_num[1] > checkin_num[1]:
                            canPrint = True
                    elif checkout_num[0] > checkin_num[0]:
                        canPrint = True
##                canPrint = False
##                if datetime.date(x[2].strip('/')) > datetime.date(x[2].strip("/")) and datetime.date(x[2]).strip("/") != datetime.date(x[2].strip("/")):
##                     canPrint = True
                else:
                     canPrint = False
                if canPrint:
                     r = Reservation(x[1], x[2], x[3], x[4], x[5])
                     list_of_reservations.append(r)
                     confirmation_num = 1
                     for i  in list_of_reservations:
                         reservation_dict[confirmation_num] = i
                         confirmation_num += 1
                     if x[1] not in reservation_dict.items(): 
                         print("Reserving room", x[1], "for", x[4], x[5], "-- Confirmation #", confirmation_num - 1)
                         print("\t(arriving", x[2], ", departing", x[3], ")")
                     else:
                        if x[1] in reservation_dict.items():
                            print("Sorry, can't reserve room", v.room_num, "(", v.checkinDate, "to", v.checkoutDate, ");")
                            print("\tit's already booked (Conf. #", k ,")")

                else:
                    print("Sorry, can't reserve room", x[1], "(", x[2], "to", x[3], ");")
                    print("\tcan't leave before you arrive.")
            else:
                print("Sorry; can't reserve room", x[1],"; room not in service")
        elif x[0].upper() == 'LR':
            print ('Number of reservations:', len(list_of_reservations))
            print('No. Rm. Arrive      Depart     Guest')
            print('------------------------------------------------')
            confirmation = 0
            for k,v in reservation_dict.items():
                print("{:3d} {:3s} {:10s} {:10s} {:15s}".format(k,v.room_num,v.checkinDate, v.checkoutDate, v.lastName  +" " + v.firstName))
                     
                
stage4()

            
                    
                
