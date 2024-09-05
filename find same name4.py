a=["D","B","E","C","A","D","H","C","C","E","F","G","B"]
b=set()

def find_same_name(a):
    n=len(a)
    for i in range (0,n):
        for j in range (i+1,n):
            if a[i]==a[j]:
                b.add(a[i])
    return b
print(find_same_name(a))
