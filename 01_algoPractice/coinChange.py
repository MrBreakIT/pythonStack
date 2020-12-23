# “Coin Change with Object
# As before, given a number of U.S. cents, return the optimal configuration of coins, in an object.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.
# -------------------------------------------------------------------------------COIN CHANGE- JoshWren
# def coin_change(coins):
#     coin_dict = {
#         'quarters': 0,
#         'dimes': 0,
#         'nicklels': 0,
#         'pennies': 0,
#     }

#     change = 0

#     while coins >= 25:
#         change = 25
#         coin_dict['quarters'] += 1
#         coins -= change
#     while coins >= 10:
#         change = 10
#         coin_dict['dimes'] += 1
#         coins -= change
#     while coins >= 5:
#         change = 5
#         coin_dict['nicklels'] += 1
#         coins -= change
#     while coins >= 1:
#         change = 1
#         coin_dict['pennies'] += 1
#         coins -= change

#     return coin_dict


# print(coin_change(99))

# --------------------------------------------------------------------------------COIN CHANGE--- Schneider_Bertrand group
# def coinChange(dinero):
#     print(' In the function')
#     quarters = 0
#     dimes = 0
#     nickels = 0
#     pennies = 0
#     realAmount = dinero
#     for i in range(dinero, -1, -1):
#         if realAmount >= 25:
#             quarters += 1
#             realAmount -= 25
#         elif realAmount >= 10:
#             dimes += 1
#             realAmount -= 10
#         elif realAmount >= 5:
#             nickels += 1
#             realAmount -= 5
#         elif realAmount >= 1:
#             pennies += 1
#             realAmount -= 1
#         elif realAmount == 0:
#             print(f"Quarters: {quarters}, Dimes: {dimes}, Nickels: {nickels}, Pennies:{pennies}")
#             return





# coinChange(137)
# --------------------------------------------------------------------------------COIN CHANGE--- EricViera
# def coinChangeObject(cents):
#     money = {"quarters": 0, "dimes": 0,"nickels": 0, "pennies":0}
#     money["quarters"] = math.trunc(cents/25)
#     cents = cents % 25
#     money["dimes"] = math.trunc(cents / 10)
#     cents = cents % 10
#     money["nickels"] = math.trunc(cents / 5)
#     cents = cents % 5
#     money["pennies"] = cents
#     return money

# print(coinChangeObject(87))
# -----------------------------------------------------------------------------COIN CHANGE--- DanielMartinez
# def coinChange(cents):
#     output = {"pennies": 0, "nickels": 0, "dimes": 0, "quarters": 0}
#     while cents > 0:
#         if cents >= 25:
#             output["quarters"] += 1
#             cents -= 25
#         elif cents >= 10:
#             output["dimes"] += 1
#             cents -= 10
#         elif cents >= 5:
#             output["nickels"] += 1
#             cents -= 5
#         elif cents >= 1:
#             output["pennies"] += 1
#             cents -= 1
#     return output
# print(coinChange(74))
# --------------------------------------------------------------------------------COIN CHANGE--- ShawnLockhart
# def coinChange(amount):

#     output = {
#         "quarter": 0,
#         "dime": 0,
#         "nickel": 0,
#         "penny": 0,
#     }
#     if amount >= 0:
#         while amount >= 25:
#             amount -= 25
#             output['quarter'] += 1
#         while amount >= 10:
#             amount -= 10
#             output['dime']+=1
#         while amount >= 5:
#             amount -= 5
#             output['nickel']+=1
#         while amount >= 1:
#             amount -= 1
#             output['penny']+=1
#     return output

# print(coinChange(336))

# --------------------------------------------------------------------------------COIN CHANGE--- RobMoore
# def optimalChange(num):
#     quarter = 25
#     quarterCount = 0
#     dime = 10
#     dimeCount = 0
#     nickel = 5
#     nickelCount = 0
#     penny = 1
#     pennyCount = 0
#     coinChange = {}

#     for i in range(num, -1, -1):
#         if num >= quarter:
#             num -= quarter
#             quarterCount += 1
#         elif num >= dime:
#             num -= dime
#             dimeCount += 1
#         elif num >= nickel:
#             num -= nickel
#             nickelCount += 1
#         elif num >= penny:
#             num -= penny
#             pennyCount += 1

#     coinChange['Quarters'] = quarterCount
#     coinChange['Dimes'] = dimeCount
#     coinChange['Nickels'] = nickelCount
#     coinChange['Penny'] = pennyCount

#     print(coinChange)

# optimalChange(49)

# --------------------------------------------------------------------------------COIN CHANGE--- JoshuaEngland
#     def giveMeChange(num):
#     output = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

#     quarter = 0
#     dime = 0
#     nickel = 0
#     penny = 0


#     while num > 0:

#         if num >= 25:
#             quarter += 1
#             num -= 25
#         elif num >= 10:
#             dime += 1
#             num -= 10
#         elif num >= 5:
#             nickel += 1
#             num -= 5
#         else: 
#             penny += 1
#             num -= 1

#     output["quarters"] = quarter
#     output["dimes"] = dime
#     output["nickels"] = nickel
#     output["pennies"] = penny

#     return output

# print(giveMeChange(95))

# print(giveMeChange(26))
# --------------------------------------------------------------------------------COIN CHANGE--- InstructorRob
def coinChange(coinInput):   
    output = {}
    q = int(coinInput/25)
    output['quarters']=q
    coinsRemaining = coinInput-(25*q)
    d =int(coinsRemaining/10)
    output['dimes']=d
    coinsRemaining = coinsRemaining-(10*d)
    n = int(coinsRemaining/5)
    output['nickels'] = n
    coinsRemaining = coinsRemaining-(5*n)
    output['pennies'] = coinsRemaining
    return output




print(coinChange(49))
# --------------------------------------------------------------------------------COIN CHANGE--- xxxxxxxxxxxxxxxx