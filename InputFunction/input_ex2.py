

# Ask user to give you a string
# Ask user to give order of the letter and print that letter from the string

print("Enter a text")
text = input()

print("Enter the order number of the letter you want to see")
order_number = int(input())

# We have to consider then user doesn't know about index numbers and number user provided will be
#1 bigger then the index number
# "Python"
# 012345  --> index number
#  123456 ---> orer number which user will think it is true

index_number = order_number -1

print(text[index_number])
