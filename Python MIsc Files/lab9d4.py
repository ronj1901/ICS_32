### pard d4


print("part d4a\n\n")
work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']
print(work_week)


def tally_days_worked (WL:list)->dict:

    new_dict = {}

    for worker in WL:
        new_dict[worker] =WL.count(worker)
    return new_dict
  
        

workers = tally_days_worked(work_week)

print(workers)


print("part d4b\n\n")

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}
print(hourly_wages)




print("****" *10)
def pay_employees(Worker:dict,hourly:dict)->None:
    worker_list = []
    days_list = []
    pay_list = []
    for i in sorted(Worker):
       worker_list.append(i)
       
    for j in sorted(Worker):
        days_list.append(Worker[j])

    for k in sorted(hourly):
        if k != 'Huey':
            pay_list.append(hourly[k])
    a=(worker_list)
    b=(days_list)
    c=(pay_list)
        
    for i in range(len(Worker)):
           print("\n{:s} will be paid {:.2f} for {:d} hours of work at ${:.2f} per hour.".format(a[i], b[i] * c[i]*8, b[i] * 8 ,c[i]))
        
   

    
    

pay_employees(workers, hourly_wages)


###d5
print("\n\npartd5", "***" * 10)


dictionary = { 'a': 1, 'b':2 }
inv_map = {v: k for k, v in dictionary.items()}
print(inv_map)

my_dict = {'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}

def reverse_dict(D:dict)->dict:
    return {v: k for k, v in D.items()}

print(reverse_dict(dictionary))

print("reversed ordered: \n",reverse_dict(my_dict))


## Alternative method
##new_dict = {}
##for k ,v  in zip(my_dict.keys(), my_dict.values()):
##    new_dict[v]= k
## 
##print(new_dict)

 
    









