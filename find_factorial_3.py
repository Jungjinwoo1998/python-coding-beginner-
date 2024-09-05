#재귀함수를 이용하여 팩토리얼을 구해보기

def fact(n):
    if n<=1:
        return 1

    return n*fact(n-1)

print(fact(10))