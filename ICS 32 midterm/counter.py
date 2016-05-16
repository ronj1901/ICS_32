# counter.py
# classes examples


class Counter:

    def __init__(self):
        ''' Initializes a counter with a count of zero'''
        self._count = 0

    def count(self)->int:
        ''' Incremens and returns the count '''
        self._count += 1
        return self._count

    def peek(self)->int:
        ''' returns the count withoout updating it '''

        return self._count

    def reset(self)->None:
        '''  Resets the counter, so that its value is 0 '''
        self._count = 0

    
