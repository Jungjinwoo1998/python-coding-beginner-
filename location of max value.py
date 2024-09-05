a = [4, 6, 13, 545, 57, 234, 445, 65675, 234, 1233, 436536, 344, 22, 11, 1, 2, 2, 34445]

def maxval(a):
    max_candidate = a[0]
    n = len(a)
    for i in range(1, n):
        if max_candidate < a[i]:
            max_candidate = a[i]
    return max_candidate

print(maxval(a))
            
        