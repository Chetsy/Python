def IterationFunction(i,value):
    value +=1
    value *=i
    return value
    


CurrentValue = 0

for iteration in range(0,10):

    CurrentValue = IterationFunction(iteration,CurrentValue)
    
    print(CurrentValue)

print("CurrentValue: {0}" .format(CurrentValue))


