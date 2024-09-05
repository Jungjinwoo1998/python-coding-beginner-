#maxval를 찾은 뒤 a위치에 있는지 검사
a=[4,234,123,2,43,5,23,5699,3,2,3,24,664,4]
b=[]
def find_maxval(a):
    max_candidate=0
    n=len(a)
    for i in range (0,n):
        if max_candidate<a[i]:
            max_candidate=a[i]
            
    print("The max value is :", max_candidate)
    
    m=max_candidate

#아이디어2: max value 위치의 뒤쪽에 있는 자료들을 전부 삭제한 뒤 0번째부터 최댓값이 있는 위치까지의 자료를 b로 새로 정의한 다음 len(b) 구하기
    
    l=0
    n=len(a)
    while m!=a[l]:
        l+=1
    
    
    for j in range (0,l+1):
        b.append(a[j])
    location=len(b)-1
    
    print("The location of max is :", location)
    return location
print(find_maxval(a))

    
    