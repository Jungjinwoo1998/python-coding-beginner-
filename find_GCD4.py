def gcd(a,b):
    while True:
        if [(a%b==0 and b%a!=0)==True or (a%b!=0 and b%a==0)==True]:
            return min(a%b,b%a)
    return gcd(a%b,b%a)

print(gcd(15,6))
print(gcd(18,10))
print(gcd(20,8))
print(gcd(72,99))
