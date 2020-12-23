# ---------------------------------------------------------------------------String is Palindrome
# “String: Is Palindrome
# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”
# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

# 1-create a function
# 2-returns a boolean whether string is a strict palindrome
# 3-for "a x a" or "racecar" return TRUE.
# 4- dont ignore spaces,punctuation,capitalization-  "Dud" or "oho!", return FALSE

# ------------------------------------------------------------------------------String is Palindrome
# def isPalindrome(string):
#     reversedString = ""
#     for i in range(len(string) - 1, -1, -1):
#         reversedString += string[i]

#     if reversedString.lower() == string.lower():
#         return True
#     else:
#         return False

#         # come back to figure out spaces...


# print(isPalindrome('Racecar'))

# ------------------------------------------------------------------------------String is Palindrome
# # ......from Austin Shoen
# def isPalindrome(str):
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True

# print(isPalindrome("racecar"))
# ------------------------------------------------------------------------------String is Palindrome
# ....from morning class
# def isPal(stringInput):
#     if stringInput != reverseString(stringInput):
#         return False
#     else:
#         return True


# print(isPal("racecar"))