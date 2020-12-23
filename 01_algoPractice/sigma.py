# def sigma(num):
#     if num<=1:
#         return 1
#     else:
        # return num

def factorial(num):
    if num <= 0:
        return 1
    return num * factorial(num-1)

print(factorial(5))   #1*2*3*4*5
print(factorial(10))  #1*2*3*4*5*6*7*8*9*10 = 3,628,800
