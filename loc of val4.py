a=[198,23,544,23,11,66,334,66,32,6599,76,454,69]

def find_maxlocation(a):
    n=len(a)
    max_location=0
    for i in range(0,n):
        if a[max_location]<a[i]:
            max_location=i
    return max_location

print(find_maxlocation(a))