#=====================================================================
#library
import time
import math
#=====================================================================
#variables

t = float(input("Please insert t(s): "))
while t < 0:
    t = float(input("t must >= 0: "))
n = int(input("Please insert n: "))
while n <= 0:
    n = int(input("n must > 0: "))
cnt = float(0)
line = 5

#=====================================================================
#main function

print("Start : %s" % time.ctime())

for i in range(0, line+1):

    print("%8.2f%% (%4d of %4d)|" %(float(round(cnt)/n*100), cnt, n), end="")

    for j in range(0, int(cnt/n*5)):
        print("=", end="")
    for k in range(int(cnt/n*5), line):
        print(" ", end="")
    print("|")


    if cnt==n:
        break
    
    cnt += math.ceil(n/line)

    time.sleep(round(n/line)*t)
    if cnt >= n:
        cnt=n

print("End : %s" % time.ctime())
