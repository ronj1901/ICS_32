

print('Course Cap Enr % Full % Wait')
print('------ --- --- ------ ------')

print("{:4s}{:5s} {:3d}{:4d}{:5.1f}% {:5.1f}%".format("ICS","31",350,2,0.6,0.0))
  
print("{:5s}b {:5s} {:4d}b {:4d}b {:5.1f}% b{:5.1f}%".format("ICS6B","31",350,2,0.6,0.0))
  



print("ANOTHER TYPE of string formatting\n\n")

counts = [1, 0, 0, 2, 2, 3, 8, 22, 33, 40, 45]
TOPSCORE = 10
for s in range(TOPSCORE + 1):
     print("{:2d}. {:3d} ({:5.2f}%)".format(s, counts[s], counts[s]/sum(counts)*100))

print(" --- " * 20)
for s in range(TOPSCORE + 1):
     print("{:2d}. {:5d} ({:5.2f}%) {:}".format(s, counts[s], counts[s]/sum(counts)*100, '*' * counts[s]))
     

print(str(121//60), str(121%60))


MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August', 'September', 'October', 'November', 'December']

def mmddyy_to_MonthDayYear(mmddyy: str) -> str:

    fields = mmddyy.split('/')
    month_number = int(fields[0])-1
    month_name = MONTHS[month_number]
    day = fields[1]

    year = '20' + fields[2]

    return month_name + " " + day + ","  + year

print(mmddyy_to_MonthDayYear('10/31/15'))

print("10/16/1991".split('/'))

 
# LIST PROCESSING

def remove_front_matter(linelist:[str])->[str]:

    dividing_line = 0
    for line in linelist:
        if line == 'END OF FRONT MATTER':
            break
        dividing_line += 1
    return linelist[dividing_line+1:]

test_list = ["To be skipped",
 "Also to be skipped",
 "END OF FRONT MATTER",
 "To be included",
 "Also to be included"]


print(remove_front_matter(test_list))


# LIST PROCESSING
quiz_scores = [18, 20, 18, 20, 0, 10, 10, 20, 10, 20]

def zero_counts(top_value: int)->[int]:

    result = list()
    for i in range(top_value+1):
        result.append(0)
    return result

print(zero_counts(11))

def count_scores(scores: 'list of int', top_score: int) -> 'list of int':
    counts = zero_counts(top_score)
    for s in scores:
        counts[s] += 1
    return counts


print(count_scores([],10))
L = [1,1,1,1,2,2,2,3,4,3,4,4,5,6,7]
uniqueL = set(L)
print(uniqueL)
uniqueL.add(0)
print(uniqueL)


# FILE

infile = open('records.txt', 'r')
inputstring = infile.read()
inputlist = inputstring.split('\n')
print(inputstring)
##DRL = [ ]
##for dr in inputlist:
##    fields = dr.split('\t')
##    if len(fields) == 3:
##         ticketlist = [ ]
##    else:
##        ticketlist = fields[3].strip().split(',')
##        Datelist = []
##    for d in ticketlist:
##        Datelist.append(mmddyy_to_Date(d))
##    reccord = DrivingRecordD.(fields[0], fields[1], int(fields[2]), Datelist)
##    DRL.append(record)
##print(DRL)
##infile.close()

def Date_to_mmddyy(D: Date) -> str: 
    return str(D.month) + "/" + str(D.day) + "/" + str(D.year[2:4])
print(Date_to_mmddyy(2051,12,12))



