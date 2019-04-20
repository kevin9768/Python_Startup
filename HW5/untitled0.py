q = [0]*5

def valid(row,col):
    for i in range(0, row):
        if q[i] == col or row-i == col - q[i] or row - i == q[i] - col:
            return False
    return True

def display():
    for i in range(0,5):
        for j in range(0,5):
            if q[i]==j:
                print("▇", end='')
            else:
                print("❏", end='')
        print()
    print()
    
def place(row):
    if row==5:
        display()
    elif row<5:
        for j in range(0,5):
            if valid(row,j):
                q[row] = j
                place(row+1)
                
place(0)