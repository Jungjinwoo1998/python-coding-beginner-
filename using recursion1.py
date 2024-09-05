#재귀 함수를 이용해서 1부터 n까지의 합 구하기

def sum(n):
    if n<=1:
        return 1
    return n+sum(n-1)
    
print(sum(10))
print(sum(1))
print(sum(6))
print(sum(5))
print(sum(-19))
