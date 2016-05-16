
grade_list = ['A', 'A', 'A','A', 'A','A','B','B','B','B','B','B']
total_units = int(input("How many units did you take?"))
def calculate_GPA(G:list)->float:

    total_GPA = 0

    for grades in G:
        if grades == 'A':
            Grade = 4.0
            total_GPA += Grade
        elif grades == 'B':
            Grade = 3.0
            total_GPA += Grade

        elif grades == 'C':
            Grade = 2.0
            total_GPA += Grade
        elif grades == 'D':
            Grade = 1.0
            total_GPA += Grade
        elif grades == 'F':
            Grade = 0.0
            total_GPA += Grade
       

    return total_GPA/total_units

print(calculate_GPA(grade_list))



   
            
