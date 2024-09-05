def gcd(a,b):
    if (a%b==0 or b%a==0)==True:
        return min(a,b)
    return gcd(a%b,b%a)
print(gcd(15,6))
print(gcd(18,9))
print(gcd(20,8))
