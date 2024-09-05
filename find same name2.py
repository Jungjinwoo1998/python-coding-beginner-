a=["D","B","E","C","A","D","H","C","C","E","F","G","B"]
b=set()


#자료들이 막 섞여있는 상태에서의 같은 값 찾기
#idea: 중복되는 자료를 set b로 옮기기

def find_same_name(a):
#같은 자료가 뭔지 인식하는 과정이 먼저
    i=1
    while len(a)!=2:
        if a[0]==a[i]:
            b.add(a[0])
            a.pop(0)
        else:
            a.pop(0)
    return b
print(find_same_name(a))
    
    