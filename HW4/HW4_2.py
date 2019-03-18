#==============================================
#variables
array = [0]*4
level = ['A','B','C','D']
N = int(input("Number of Students: "))
while N <= 0:
    N = int(input("Please insert a positve number: "))
temp = int

#==============================================
#function

def classify(x):
    if x>=87:
        array[0] += 1
    elif x>=75:
        array[1] += 1
    elif x>=65:
        array[2] += 1
    else:
        array[3] += 1
    return

#==============================================
#main function

for i in range(0, N):
    print("Score #%d : "%(i+1), end="")
    temp = int(input())
    while temp < 0 :
        temp = int(input("Please insert a positive number: "))
    classify(temp)

print("Grade    Frequency     Bar Chart")

for i in range(0, 4):
    print("    %c    %9d     " %(level[i],array[i]), end="")
    for j in range(0, array[i]):
        print("*", end="")
    print()
