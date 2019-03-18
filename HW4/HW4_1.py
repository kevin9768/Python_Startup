#=====================================================
#variables
D = int(input("D: "))
while D<=0:
    D = int(input("D must be a positive integer: "))
array = [0]*D
temp = int

#=====================================================
#main function
temp = int(input("insert -1 to end: "))

while temp!=-1:
    array[temp%D] += 1
    temp = int(input("insert -1 to end: "))

for i in range(0, D):
    print("%d "%array[i], end="")