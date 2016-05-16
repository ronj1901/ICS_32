


# recurisve function that returns the smallest value in a nested_list

def recursive_min(nested_list : [[]])->int:

    for item in nested_list:

        minimum = i
        if type(item)  == list:

            // sometinh
        else:
            if  i < minimum:
                i = minum

    
    return minimum 


test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)


