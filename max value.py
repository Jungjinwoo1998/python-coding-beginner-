
#값들이 순서대로 배열되어있지 않는 경우
b=[5,7,8,15,65,24,76,1255,45,87,43,3000,44,3500,1600]


def find_max_val(m):
    n=len(m)
    max_candidate=b[0]
    for i in range (1,n+1):
        if max_candidate<b[i-1]:
            max_candidate=b[i-1]
            print(max_candidate)
    return
    

find_max_val(b)        