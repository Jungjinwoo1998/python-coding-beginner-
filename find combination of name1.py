a=['A','B','C','D','E','F']
def combi_of_name(a):
    n=len(a)
    first_of_combi=0
    second_of_combi=0
    for i in range (0,n-1):
        for j in range (i+1,n):
            first_of_combi=a[i]
            second_of_combi=a[j]
            print(first_of_combi, '-', second_of_combi)
    return a
print(combi_of_name(a))