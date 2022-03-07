myList = list([13,3,12,24,56,5,-256])

for element in myList:
    print(element)
    pass

listlength = len(myList)

print("second Attempt")

for iteration in range(0,listlength):
    print("Index: {0} Value: {1}".format(iteration,myList[iteration]))

firstValue = 2
secondValue = -5



# Equality Operator 
print(firstValue == secondValue)

print(firstValue < secondValue)   

print(firstValue > secondValue)  