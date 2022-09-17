

s = "Python"
print(s.upper()) # -> PYTHON

print(s)        #  -> Python
# Since the string in immutable, it will not change it value unless it is reassigned

# Bardygyn kichine tamga kylabyz desek tomondogudoi kylyp chygarabyz
s = "PYthon"
print(s.lower())

# Baaryn chon tamga m kylabyz desek tomondogudoi kylabyz
print(s.lower(). upper())
# Method chaining -> as long as the method you use in the string returns another string 
# You can use other string methods
print(s.lower(). upper()) # s will be printed in all upper case since it is the last method
print(s.upper().lower())  # s wil be printed in all upper case since it is the last method


#SWAP CASE METHOD- almashtyruu metodu. chon tamgany kichine, kichine tamgany chongo 
# almashtyrat. misaly tomondogudoi
print("Result of swap case method",s.swapcase())

#CAPITALIZE METHOD- bir gana bashky tamgany chon tamgaga almashtyrat. misaly tomondogudoi
print("Result of capitalize method",s.capitalize())





