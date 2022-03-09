Problem Description

Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

For example
5 = 2 + 3,
17 = 2 + 3 + 5 + 7,
41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000





n =int(input()) 
prime_list = []

# creating prime number list
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime_list.append(i)
#-------------------


#check whether number satosfoes the condition
def count_prime(no):
    sum = 0
    for i in range(len(prime_list)):
        sum+=prime_list[i]
        if sum==no:
            return True
    else:
        return False
        
#driver code   
cnt = 0
for i in range(3,n+1):
    if i in prime_list:
        if count_prime(i):
            cnt+=1
print(cnt)
