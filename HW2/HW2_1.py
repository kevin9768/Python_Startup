#===========================================
#Variables
Year = int(input("Insert year: "))
while Year < 0:
    Year = int(input("Please insert a number larger than 0: "))
Month = int(input("Insert month: "))
while Month < 1 or Month > 12:
    Month = int(input("Please insert a number between 1 and 12: "))
First = int(input("Insert first: "))
while First < 0 or First > 6:
    First = int(input("Please insert a number between 0 and 6: "))
Total_days = None

#===========================================
#main function
if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
    Total_days = 31
elif Month == 2:
    if(( Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0 and Year % 3200 != 0)):
        Total_days = 29
    else:
        Total_days = 28
else:
    Total_days = 30

print(" Su Mo Tu We Th Fr Sa")
print("=====================")

for i in range(0, First):
    print("   ",end="")

for i in range(1, Total_days+1):
    if First % 7 == 6:
        print("%3d" %i)
    else:
        print("%3d" %i,end="")
    First += 1

