a=["A","A","B","C","D","D"]
b=[]
#이웃한 위치에 같은 자료가 위치한 경우

def find_same_neighborhood(a):
    n=len(a)
    for i in range (1,n):
        if a[i-1]==a[i]:
            b.append(a[i])

    return b

print(find_same_neighborhood(a))