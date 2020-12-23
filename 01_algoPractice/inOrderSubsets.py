# Create strSubsets(str). Return an array with every possible in-order character subset of str. The resultant array itself need not be in any specific order – it is the subset of letters in each string that must be in the same order as they were in the original string. Given "abc", return an array that includes ["", "c", "b", "bc", "a", "ac", "ab", "abc"] (in any order).”


# # str : Stores input string 
# # curr : Stores current subset 
# # index : Index in current subset, curr 
# def powerSet(str1, index, curr): 
#     n = len(str1) 

#     # base case 
#     if (index == n): 
#         return

#     # First print current subset 
#     print(curr) 

#     # Try appending remaining characters 
#     # to current subset 
#     for i in range(index + 1, n): 
#         curr += str1[i] 
#         powerSet(str1, i, curr) 

#         # Once all subsets beginning with 
#         # initial "curr" are printed, remove 
#         # last character to consider a different 
#         # prefix of subsets. 
#         curr = curr.replace(curr[len(curr) - 1], "") 

#     return

# Driver code 
# if __name__ == '__main__': 
#     str = "abc"; 
#     powerSet(str, -1, "") 

#////////////////////////////////////////////////////////////////////
from collections import deque

# Recursive function to print all distinct subsets of S
# S   --> input set
# out --> list to store subset
# i   --> index of next element in set S to be processed
def findPowerSet(S, out, i):

	# if all elements are processed, print the current subset
	if i < 0:
		print(list(out))
		return
	# include current element in the current subset and recur
	out.append(S[i])
	findPowerSet(S, out, i - 1)
	# exclude current element in the current subset
	out.pop()	   # backtrack
	# remove adjacent duplicate elements
	while i > 0 and S[i] == S[i - 1]:
		i = i - 1

	# exclude current element in the current subset and recur
	findPowerSet(S, out, i - 1)

# Program to generate all distinct subsets of given set
if __name__ == '__main__':

	S = ["P", "y", "t", "h" ,"o", "n"]

	# sort the set
	S.sort()

	# create an empty list to store elements of a subset
	out = deque()
	findPowerSet(S, out, len(S) - 1)

#///////////////////////////////////////////////////////////////////////////////////////////////////
#             from Rahb
def ios(string, sub = "", i=0):
    if i == len(string):
        return [sub]
    else:
        return ios(string, sub + string[i], i+1) + ios(string, sub, i+1)


print(ios("abcd"))




