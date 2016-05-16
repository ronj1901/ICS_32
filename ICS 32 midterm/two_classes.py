class MultiplyByCalc:

    def __init__(self, multiplier):
        self._multiplier  = multiplier 

    def calculate(self, n):
        return n * self._multiplier
        


class LengthCalc: 

    def calculate(self, s):      

        return len(s)

def run_calcs(calcs: ['Calc'], starting_value):

    current_value = starting_value

    for calc in calcs:

        current_value = calc.calculate(current_value)
       

    return current_value 

if __name__ == '__main__': 

    print(run_calcs([MultiplyByCalc(2), LengthCalc(), MultiplyByCalc(7)], 'Boo'))


    
