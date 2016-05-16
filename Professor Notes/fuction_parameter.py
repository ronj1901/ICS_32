# taking function as a parameter and appennding in list:


def square (n: 'number') -> 'number':
    return n * n



def cube(n:'number')->'number':
    return n * n * n


def apply_to_all(f:'one_argument function', elements:list)->list:


    results = []

    for element in elements:
        results.append(f(element))

    return results

class Counter:
    def __init(self):
        self._count = 0
    def count(self) -> int:
        self._count += 1
        return self._count

    def reset(self, new_count:int)->None:
        self._count =  new_count

    


