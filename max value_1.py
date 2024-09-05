a = [4, 6, 13, 545, 57, 234, 445, 65675, 234, 1233, 436536, 344, 22, 11, 1, 2, 2, 34445]

def maxval(a):
    max_candidate = a[0]
    i = 1
    while i < len(a):
        if max_candidate < a[i]:
            max_candidate = a[i]
            # Swap the max_candidate to the 0th position
            a[0], a[i] = a[i], a[0]
            i+=1
        else:
            a.pop(i)
    return max_candidate

print(maxval(a))