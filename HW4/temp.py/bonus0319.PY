a = int(input("a: "))
b = int(input("b: "))

record = 0

for i in range(a, b+1):
    temp = str(i)
    flag = 0
    for j in range(0, len(temp)):
        if int(temp[j]) == 0:
            flag = 1
            break
        if i % int(temp[j]) != 0 :
            flag = 1
            break
    if flag == 0:
        if record == 0:
            print("%d" %i, end="")
        else:
            print(", %d" %i, end="")
        record += 1

    