def sum_numbers(numlist: [int] ) -> int:
    ''' Adds up the integer in a list of integers'''
    total = 0
    for num in numlist:
        total += num

    return total

assert(sum_numbers([1,2,3])) == 6



def sum_numbers2(numlist: [[int]]) -> int:
    '''Adds up the integers in a list of lists of integers'''
    total = 0

    for sublist in numlist:
        for num in sublist:
            total += num

    return total

print(sum_numbers2([[5,5,4,3,52,2]]))


def sum_numbers3(numlist: [int or [int]]) -> int:
    '''
    Adds up the integers in a list whose elements are either integers or
    lists of integers
    '''
    total = 0

    for element in numlist:
        if type(element) == list:
            for num in element:
                total += num
        else:
            total += element

    return total
