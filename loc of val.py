#최댓값 뒤에 있는 자료들은 모두 "삭제"해버린다. 그것이 나의 알고리즘.
a=[4,234,123,2,43,5,23,5699,3,2,3,24,664,4]
def find_maxlocation(a):
    max_candidate=0
    num_of_max=0
    n=len(a)
    
    for i in range (0,n):
        if max_candidate<a[i]:
            max_candidate=a[i]
    #요까지가 max value구하기 과정이었음.
    print("Is max value exists?(of course!) :",max_candidate in a)
    print("The max value is :", max_candidate)
   
    #이제부터는 max value의 번호가 몇번인지 찾을거임.
    while num_of_max<len(a):
        if max_candidate!=a[num_of_max]:
            num_of_max+=1
        else:
            print("The location of max is :", num_of_max)
            return num_of_max
        
print(find_maxlocation(a))