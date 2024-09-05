a=["D","B","E","C","A","D","H","C","C","E","F","G","B"]
b=set()
c=set()
#자료들이 막 섞여있는 상태에서의 같은 값 찾기
#a에 있는 자료들을 set b로 옮기고, 만약에 b의 len값이 늘어나지 않았다면 c에 그 값을 추가한다. 최종적으로 c의 값이 중복된 값
def find_same_name(a):
    m=1
    n=len(a)
    for i in range (0,n):
        b.add(a[i])
        if m!=len(b):
            c.add(a[i])
        else:
            m+=1
        
    return c
print(find_same_name(a))

            