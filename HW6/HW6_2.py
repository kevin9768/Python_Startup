#====================================================
#Library
import random as rd

#====================================================
#Variables
ans = str
user = str

#====================================================
#Functions
def generate_ans():
    _ans = []
    idx = 0
    while idx<4:
        if idx>0:
            temp = rd.randint(0,9)
        else:
            temp = rd.randint(1,9)
        flag = 0
        for i in range(0, idx):
            if temp==int(_ans[i]):
                flag = 1
                break
        if flag==1:
            continue
        _ans.append(str(temp))
        idx += 1

    return ''.join(_ans)
    

def valid(a):
    if int(a)/10000 >= 1:
        return False
    if int(a)/1000 < 1:
        return False
    for i in range(0,4):
        for j in range(i+1,4):
            if a[i]==a[j]:
                return False
    return True
    

def check(a, g):    
    A = 0
    B = 0
    for i in range(0,4):
        if a[i]==g[i]:
            A += 1
    for i in range(0,4):
        for j in range(0,4):
            if g[j]==a[i]:
                B += 1
    B -= A
    if A==4:
        print("Correct!")
        return True
    else:
        print("Guess: %s; Result: %dA%dB" %(g, A, B))
        return False
    
#====================================================
#Main Function
ans = generate_ans()
while True:
    while True:
        user = input("請猜四位數字: ")
        if valid(user):
            break
        else:
            print("Input invalid!:")
    if check(ans, str(user)):
        break
    
