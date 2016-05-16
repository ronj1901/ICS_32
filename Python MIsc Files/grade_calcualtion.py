
infile = open("finalGrades.txt", 'r')

data  = infile.readlines()
total_A = 0
total_D  = 0

for lines in data:
    
    line = lines.split()
    for i in line:
        if i == 'A' or  i == 'A-' or  i == 'A+':
            
            total_A += 1
        if i == 'D':
            total_D += 1
            
print(total_A)
print(total_D)
        

