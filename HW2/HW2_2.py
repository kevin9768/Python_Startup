#===========================================
#Variable
N = int(input("Insert the length of your fibonacci series: "))
while N <= 0:
    N = int(input("Please enter a positive integer: "))

#===========================================
#functions
def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-2)+fib(a-1)

#===========================================
#main function

for i in range(0,N):
    print (fib(i), end="")
    print (" ", end="")

