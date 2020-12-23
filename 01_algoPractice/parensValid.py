# ------------------------------------------------------------------------------Parens Valid-----------------------------------------------------------------------------------------------------
# “ Parens Valid
# Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed. Given "N(0)t )0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

# -------------------------------------------------------------------------------------------Googled solution
# class py_solution:
#     def is_valid_parenthese(self, str1):
#         stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
#         for parenthese in str1:
#             if parenthese in pchar:
#                 stack.append(parenthese)
#             elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
#                 return False
#         return len(stack) == 0

# print(py_solution().is_valid_parenthese("(){}[]"))
# print(py_solution().is_valid_parenthese("()[{)}"))
# print(py_solution().is_valid_parenthese("()"))

# -------------------------------------------------------------------------ParensValid  --Class solutions- JoshWren
# def parenthesesChecker(input):
#     openCount = 0
#     closeCount = 0
#     for character in range(len(input)):
#         if input[character] == ")" and openCount <= closeCount:
#             return False
#         elif input[character] == ")" and closeCount < openCount:
#             closeCount += 1
#             # print(f"close: {closeCount}, open: {openCount}")
#         elif input[character] == "(":
#             openCount += 1
#             # print(f"close: {closeCount}, open: {openCount}")
#     if openCount == closeCount:
#         return True
#     return False


# print(parenthesesChecker("Y(3(p)p(3)r)s"))

# -----------------------------------------------------------------------------ParensValid  --Class solutions- Robert Santos

# def perensValid(var):
#     state= True
#     counter1= 0
#     counter2= 0
#     for i in range(0,len(var),1):
#         print(var[i])
#         if var[i] == "(":
#             counter1 += 1
#             print("counter1", counter1)
#         if var[i] == ")" and counter1 > counter2:
#             counter2 += 1
#             print("counter2", counter2)
#         elif var[i] == ")" and counter1 <= counter2:
#             state = False
#             return state
#     if counter1 == counter2:
#         state= True
#     else:
#         state= False
#     print(counter1, counter2, state)


# testStr="Y(3(p)p(3)r)s"
# testStr1=")(()())"
# testStr2="N(0)t )0(k"
# perensValid(testStr)
# x= perensValid(testStr1)
# y= perensValid(testStr2)
# print(x)
# print(y)

# ------------------------------------------------------------------------------ParensValid  --Class solutions- ShawnLockart

# def parensValid(str):
#     parenCounter = {
#         "(": 0,
#         ")": 0
#     }

#     for chars in str:
#         if chars == ")":
#             parenCounter[chars] += 1
#             if parenCounter[")"] > parenCounter["("]:
#                 return False
#         elif chars == "(":
#             parenCounter[chars] += 1

#     if parenCounter[")"] == parenCounter["("]:
#         return True
#     else:
#         return False


# print(parensValid("Y(3(p)p(3)r)s"))
# print(parensValid("Y(3(p)p(3)r)s"))
# print(parensValid("Y(3(p)p(3r)s"))
# ------------------------------------------------------------------------------ParensValid  --Class solutions- ClassInstructor- Rob
# NOTE: must also take into account any premature closing or opening parens (if a closing parens come before an open parens)

# def parensValid(input):
#     opencount = 0
#     closedcount = 0
#     for i in range(0, len(input), 1):
#         if input[i] == "(":
#             opencount+=1
#         elif input[i] == ")":
#             closedcount +=1
#         if closedcount > opencount:
#             return False
#     if opencount != closedcount:
#         return False
#     else:
#         return True


# print(parensValid("()()"))
# print(parensValid("((())"))
# print(parensValid(")("))