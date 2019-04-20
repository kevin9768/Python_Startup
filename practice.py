a = [5,8,5,4,5,2,3,2,1]

def mean(arr):
    temp = 0
    for i in range(0, len(arr)):
        temp += arr[i]
    return temp/len(arr)

def median(arr):
    arr.sort()
    return arr[int(len(arr)/2))]
    
def mode(arr):
    return 0


print("Mean = %.2f" %mean(a))
print("Median = %.2f" %median(a))
print("Mode = %.2f" %mode(a))