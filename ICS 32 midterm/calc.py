# calculator_classes


# i wanna make a program that multiplies first with given parameter , and then the
# value produce is divided by 3



class MultiplyCalc:

    def __init__(self,multiplier):

        self._multiplier = multiplier

    def Calculate(self,n):
        return n * self._multiplier


class DivideCalc:


    def Calculate(self, n,s):
        return n * s




def run_calcs(calcs:['list of calc'], start_value):


    current_value = start_value

    for calc in calcs:
        current_value = calc.Calculate(current_value)

    return current_value

if __name__ == "__main__":

    print(run_calcs([MultiplyCalc(4), DivideCalc(1)], 10 ))

    
