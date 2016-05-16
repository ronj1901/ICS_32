 ##QUIZ 10


from collections import namedtuple
Score = namedtuple('Score', 'p1 p2')
TOPSCORE = 20


scorelist = [Score(p1=0, p2=0),
 Score(p1=1, p2=1),
 Score(p1=1, p2=5),
 Score(p1=4, p2=2),
 Score(p1=5, p2=0)]

# Initialize the table to a 20-by-20 table of blanks
table = [ ]
for row in range(TOPSCORE+1):
     table_row = [ ]
     for col in range(TOPSCORE+1):
         table_row.append(' ')
     table.append(table_row)
# Populate the table with an asterisk for each student's two scores. (When two
# students have the same pair of scores, just one asterisk appears.)
for s in scorelist:
     table[s.p2][s.p1] = '*'
# Print the 20-by-20 table
for row in range(TOPSCORE,-1,-1):
    for col in range(TOPSCORE+1):
        print(table[row][col], sep='', end='')
    print() # Print the default end= character, a newline


def tally_names(L: [str]) -> dict:
 ''' Return a dictionary with each unique string in L as the key and
 the number of times that string occurs in L as the value.
 '''
 result = { }
 for s in L:
     if s in result: 
        result[s] += 1
     else:
        result[s] = 1
 return result
assert tally_names(NL) == {'Sam': 2, 'Jill': 2, 'Joe': 5, 'Jane': 3, 'John': 1}

NL = ['Joe', 'Sam', 'Joe', 'Jill', 'Joe', 'Joe', 'Jill', 'Sam', 'Jane', 'Jane', 'Jane', 'Joe', 'John']
def dict_to_list(d: dict) -> 'list of [key, value] pairs':
    result =  []
    for key in d:
        result.append([key, d[key]])
    return result
                      

print(dict_to_list(tally_names(NL)))



def second_item(L:list)-> 'any' :
    ''' Return second field (L[1]) of a list, to use with key= in Sort() method
    '''
     return L[1]

list_of_string_frequency_pairs = dict_to_list(tally_names(NL))
list_of_s_f_pairs sort second item
most_frequent_paoit = list_of_string_frequency_pairs[0]
print("The string '", most_frequent_pair[0], "' occurs ", 
 most_frequent_pair[1], ' times.', sep='')  

    
