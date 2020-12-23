# ------------------------------------------------------------------------------Acronyms  --Class

# “Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given " there's no free lunch  -  gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.
# "missing in action" -> M.I.A.     "national hockey league" ->N.H.L

# def returnAcronym(string):
#     newstring = ""
#     for i in range(len(string)):
#         if string[0] != " ":
#             newstring= string[0]
#         if string[i] == " ":

# returnAcronym("national basketball")
# ------------------------------------------------------------------------------Acronyms  --Giang Lam

# def acro(input):
#     newStr = ""
#     newStr += input[0]
#     for i in range(len(input)-1):
#         if input[i] == " ":
#             newStr += input[i+1]
#         newStr = newStr.upper()
#     return newStr

# print(acro("Live from New York, it's Saturday Night!"))
# ------------------------------------------------------------------------------Acronyms  --Giang Lam
# def acronyms(stringInput):
#     acronym = ""
#     for i in range(len(stringInput)):
#         if stringInput[i] == stringInput[0]:
#             acronym += stringInput[i].upper()
#         elif stringInput[i - 1] == " ":
#             if stringInput[i].isalpha():
#                 acronym += stringInput[i].upper()
#         if stringInput[i] == "-":
#             acronym += stringInput[i].upper()
#     return acronym
# ------------------------------------------------------------------------------Acronyms  --Shawn Lockhart

# def acronym(string):
#     newstring = ""
#     if string[0] != " ":
#         newstring += string[0]
#     for i in range(len(string)):
#         if string[i] == " ":
#             newstring += string[i+1]
#     return newstring.upper()


# print(acronym("united states marine corps"))
# ------------------------------------------------------------------------------Acronyms  --JamesRavencroft
# newString = ""
# phrase_split = string.split()

# for i in phrase_split:
#     newString += i[0].upper()

# print(newString)
# acro("Central Inteligence Agency")
# ------------------------------------------------------------------------------xxxxxxxxxxxxxxxxxxxxxxxx
# testStr=" there's no free lunch  -  gotta pay yer way. "
# testStr1="Live from New York, it's Saturday Night!"
# def acryonyms(var):
#     newLst=''
#     if var[0] != ' ':
#         newLst += var[0]
#     for i in range(1,len(var),1):
#         if var[i-1] == ' ':
#             newLst += var[i]
#     print(newLst.upper())

# acryonyms(testStr)
# acryonyms(testStr1)

# ------------------------------------------------------------------------------Acronym- JoshWren
# def turn_to_acronym(input):
#     words = input
#     acronym = ''.join(word[0] for word in words.upper().split())
#     return acronym


# print(turn_to_acronym("central intelligence agency whatever"))
# print(turn_to_acronym("saturday night live"))
# print(turn_to_acronym("central intelligence agency"))
# print(turn_to_acronym("federal bureau investigations"))
# print(turn_to_acronym("national football league"))
# ------------------------------------------------------------------------------Acronym- JonathanKohen

# def acro(str):
#     acronym = f"{str[0]}"
#     for i in range(len(str)):
#         if str[i] == " ":
#             acronym += (str[i + 1])
#     return acronym
# print(acro("national hockey league"))
# ------------------------------------------------------------------------------ AshleyBrown
# def acro(string):
# words = “Aint nobody got time for that!”
# acronym = ‘’.join(word[0] for word in words.upper().split())
# print(acronym)
# ---------------------this is a different part???maybe but lower works
# my_name = "John Pike"
# var_name = my_name.split()
# print(var_name)
# print(''.join(var_name))
# --------------------------------------------------------------------------------from InstructorRob

# def acronyms(somestring):
#     string2 = ""
#     if somestring[0] != " ":
#         string2 += somestring[0]

#     for i in range(0, len(somestring)-1, 1):
#         if somestring[i+1] != " " and somestring[i] == " ":
#             string2 += somestring[i+1]
#     string2 = string2.upper()
#     return string2


# print(acronyms("national basketball association"))