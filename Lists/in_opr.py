
list = [2,3,5,True,"s"]

print(len(list))# 5

print(list[4]) # s

print(type(list)) #<class 'list'>

print(type(list[3])) #<class 'bool'>

print(type(list[4])) # <class 'str'>
print(type(list[2])) #<class 'int'>

# Slicing the list
print(list[1:4]) # [3, 5, True]
print(type(list[1:4])) # <class 'list'>

print(list[0:3]) # [2, 3, 5]
print(type(list[0:3])) # <class 'list'>

print(list[:2]) # [2,3]
print(list[2:]) # [5,True,'s']



# Using in operator we can specified value is in the list or not.
# We can also use in operator for strings as well.

list =[1,2,3,4,5]

if 2 in list:
    print("2 is in the list ")

if 11 in list:
    print("11 is in the list.") # This lline will not work because
    # 11 is not in the list .

# not in operator will check if the specified value is not in the 
# iterable objects. 

if 6 not in list:
    print( 6, "is not in the list")



# Using in operator we can specified value is in the list or not.
# We can also use in operator for strings as well.

list = [1,2,3,4,5]

if 2 in list:
    print("2 is in the list ")
if 11 in list:
    print("11 is in the list.") # This lline will not work because
    # 11 is not in the list .
# not in operator will check if the specified value is not in the 
# iterable objects. 
if 6 not in list:
    print( 6, "is not in the list")

# ask user to enter a random digit 
# check if the digit is present in our list or not.
# if user enters present element print you won a prize,
# if not, print maybe, next time. 
print("Enter a random digit")
digit = int(input())

if digit in list:
    print("You have won a prize")
elif digit not in list:
    print("Maybe, next time.")

# in operator can be used for every iterable object