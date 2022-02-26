"""
Write a program that takes two strings S1 and S2 as input (one per line). 
The program checks if the string S1 can be created by rearranging the characters of the string S2 and vice versa. 
If yes, the program should print YES, otherwise print NO.
The program should ignore the case sensitivity of characters.


Sample input 1:
bat
Tab

Sample Input 2:
abcaaa
aabaca

Sample Output 1:
YES

Sample Output 2:
NO
"""


import itertools

a =input().lower()
b=input().lower()


perm= list((itertools.permutations(b)))

li1= ["".join(p) for p in  perm]

if a in li1:
	print("YES")
else:
	print("NO")
