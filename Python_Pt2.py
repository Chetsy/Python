# Function for adding two values together, and return result
def AdditionFunction(A,B):
    result = A+B
    print(result)
    return result

def PrintCurrentValue():
    print(CurrentValue)


#Variable for keeping track of the current value
CurrentValue = 0

CurrentValue = AdditionFunction(CurrentValue,3)
CurrentValue = AdditionFunction(CurrentValue,1) 
CurrentValue = AdditionFunction(CurrentValue,7) 
   
PrintCurrentValue()

