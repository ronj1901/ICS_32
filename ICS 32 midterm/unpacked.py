
import powers


# write a recursive function that takes as input a nested list of strings, and returns
#a single string with each word separated by a space.


##
##def nested_build(nested_list:[str or [str]]) ->str:
##
##
##    unpacked = ''
##    for element in nested_list:
##        if type(element) == str:
##            unpacked += element + ' '
##        else:
##            unpacked += nested_build(element)
##    return unpacked
##
##print(nested_build(['Boo', ['is', 'happy', ['today']]]))
##

# these both functions work perfectly


def nested_build(nested_list:[str or [str]]) ->str:


    unpacked = ''
    for element in nested_list:
        if type(element) == list:
            unpacked += nested_build(element)
        else:
            unpacked += element +  " " 
    return unpacked

print(nested_build(['Boo', ['is', ["Nani", "Kaji Karki"],'happy', ['today']]]))


def sum_numbers(numlist:[int or [int]]) ->int:


    total = 0

    for item in numlist:
        if type(item) == list:
            for num in item:
                total += num

        else:
            total += item

    return total


print(sum_numbers([4,5,[1,2]]))


def nested_sum(nested_list: 'nested list of integers')->int:
    ''' adds up the integers in a nested list of integers'''

    total = 0

    for element in nested_list:
        if type(element) == int:
            total += element
        else:

            total += nested_sum(element)
                
    return total


print(nested_sum([3, 6, 4]))


def read_and_square() -> None:

  while True:

      number = input('Number: ')

      if number != 'exit':

        try:

          squared = powers.square(number)

          print('{} squared = {}\n'.format(number, squared))

        except:

          print('{} cannot be squared.\n'.format(number))

      else:

        break

read_and_square()


