## Every math operation between float and int data type will result in float data type

floatNum=3.0
intNum =5

print("Type of floatNum is",type(floatNum))
print("Type of intNum is",type(intNum))

addion = floatNum + intNum
print("Addition of float and int is",type(addion))

subtraction = intNum - floatNum
print("Subtraction between int and float is",type(subtraction))

multiplication = floatNum * intNum
print("Multiplication between int data type and float is",type(multiplication))

division= intNum / floatNum
print("Division between float and int data type is",type(division))

remainder = floatNum % intNum
print("The remainder between float and int data type is",type(remainder))


#There is only one way to get int which is using //
division = intNum // floatNum
print("The integer symbol division result between float and integer is",type(division))

square_of_float=floatNum * floatNum
print(type(square_of_float))