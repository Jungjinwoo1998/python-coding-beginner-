a = [4, 6, 13, 545]

def maxval(a):
    max_candidate = a[0]
    i = 1
    while i < len(a):
        if max_candidate < a[i]:
            max_candidate = a[i]
            a[0], a[i] = a[i], a[0]
            # i += 1 없어서 무한 루프 발생 가능
        else:
            a.pop(i)
    return max_candidate

print(maxval(a))