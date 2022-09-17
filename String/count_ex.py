
# Ask user to give two different string values
# If the first string contains th e second string
# return True, if not return False

print("Enter first string")
s1= input()

print("Enter second string")
s2 = input()

# If the first string doesn't contain the second string 
# count of second string in the first one should be 0

#bul uchun biz booleon functiondy koldonobuz. 0 korsotso false chygat. 1di koprsotso true chygat. 
#1-sozgo ekinchi soz okshoshso je jok degende bashky eki tamgasy okshoso anda true chygat, antkeni true 
# 1 jana birden kop korsotkon sanga chygat.

count_of_second = s1.count(s2)
is_contain = bool(count_of_second)
print(is_contain)


