

#len() function allows us to learn ho wmany charachters used to create string.
# lenght function counts spaces as well

str = "Techtorial"
str1 = " Techtorial "

print(len(str))

print(len(str1))

# Lenght function will return an integer value so we can assign integer variables using lenghtn function
lenght_of_the_str = len(str)
print(lenght_of_the_str)
print(type(lenght_of_the_str))

#create a program to print True if the lenght of str is even number
#Even number can be divided by 2
is_lenght_even = lenght_of_the_str % 2 ==0
print(is_lenght_even)