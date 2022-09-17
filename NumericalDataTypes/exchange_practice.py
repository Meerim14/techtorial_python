
# Create a python program to give most efficient exchange possible using only  coins

#quarter 25 cent
# nickel 5 cents
# dime is 10 cent
# penny 1 cent
# 2.34 cent of exchange
# 9 quarters
# 0 dimes
# 1 nickel
# 4 pennies
# $1.89
# 7 quarters 1dimes and 0 nickels 4 pennies

dollar = 2.96
dollar_amunt = dollar * 100

dollar_amount =2.96

quarter_value= .25
dime_value = .10
nickel_value = .05
penny = 0.01
    #2.96     //    .25  11

count_of_q = dollar_amount // quarter_value

print("We need to give back",count_of_q,"quarters")
    #  2.96 % 25   2.75  .21

remaining_exchange_after_q = dollar_amount % quarter_value

count_of_d =remaining_exchange_after_q // dime_value
print(count_of_d , "dimes")

remaining_exchange_after_d = remaining_exchange_after_q % dime_value
count_of_nickel = remaining_exchange_after_d // nickel_value
print(count_of_nickel, "nickels")
remaining_after_nickel = remaining_exchange_after_d % nickel_value

count_of_pennies = remaining_after_nickel // penny
print(count_of_pennies,"pennies")
