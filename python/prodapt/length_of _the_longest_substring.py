"""
Write a program that takes an integer M as input in the first line and M strings as input (one per line).
For each inputted string, the program finds the length of the longest substring that is a palindrome.
There may be more than one substring that is palindromes and are of the longest length, but your program needs to print only the length of the longest substring.

Note that palindromes are not case-sensitive.

Sample Input 1

wassamassdaw
movie
pass
Wow

Sample Output 1

7
1
2
3

"""



M = int(input())
ip=[]
for i in range(M):
	ip.append(input().lower())
	

for i in ip:
	a =i 
	li=[1]
	for j in range(len(a)):
		b = a[j:]
		if b==b[::-1]:
			li.append(len(b))
	print(max(li))
