#===========================
#variables

n = int(input("n: "))
while n<=0:
    n = int(input("n should be a positive integer: "))
m = int(input("m: "))
while m<=0 or m>n:
    m = int(input("m should be a positive integer and less or equal to n: "))
total = 0

#===========================
#functions

def c(n,m):
    if m==0 or n==m:
        return 1
    return factorial(n)/(factorial(n-m)*factorial(m))

def factorial(n):
    sum = 1
    while n > 0:
        sum *= n
        n -= 1
    return sum

#===========================

for i in range(0, m+1):
    total += c(n,i)

print("The total is %d" %total)