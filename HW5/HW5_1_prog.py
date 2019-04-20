#build all posibilities
#==========================================
origin = []

for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 5):
            for l in range(0, 5):
                for m in range(0, 5):
                    temp =[[0 for n in range(5)] for o in range(5)]
                    temp[0][i] = 1
                    temp[1][j] = 1
                    temp[2][k] = 1
                    temp[3][l] = 1
                    temp[4][m] = 1
                    origin.append([temp[0],temp[1],temp[2],temp[3],temp[4]])

result = []

#functions
#==========================================

def v_vertical(a):
    t = 0
    for i in range(0, 5):
        t = 0
        for j in range(0, 5):
            t += a[j][i]
        if t > 1 :
            return False
    return True

def v_diagonal(a):
    t = 0
    for i in range(-3, 4):
        t = 0
        for j in range(0, 5):
            if i+j<0 or i+j>4:
                continue
            t += a[j][i+j]
        if t > 1:
            return False
    for i in range(1, 8):
        t = 0
        for j in range(0, 5):
            if i-j<0 or i-j>4:
                continue
            t += a[j][i-j]
        if t > 1:
            return False
            
    return True

#main function
#==========================================
   
for i in origin:
    if v_vertical(i) and v_diagonal(i):
        result.append(i)
        
for i in result:
    for j in range(0,5):
        for k in range(0,5):
            if i[j][k] == 1:
                print("▇", end='')
            else:
                print("❏", end='')
        print()
    print()
