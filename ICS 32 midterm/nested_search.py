
# nested_search practice question

def nested_search(nested_list:[str or [str]], search:str) -> int:

    count  = 0

    for element in nested_list:
        if type(element) == type([]):
            count += nested_search(element, search)
        elif element[0].lower == search.lower:
            count += 1
 
    return count


print(nested_search(['Boo', ['is', 'happy', ['today']]], 'B'))

print(nested_search([['shambhu'], ['s '], 'y', ['name']], 's'))



import powers 

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

            


