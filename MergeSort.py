def Divide(arr, l, r):
    if l < r:
        m = (l + r) // 2
        Divide(arr, l, m)
        Divide(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr


def merge(arr, l, m, r):
    s1 = m - l + 1
    s2 = r - m

    L = [0] * s1
    R = [0] * s2

    for i in range(0, s1):
        L[i] = arr[l + i]

    for j in range(0, s2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < s1 and j < s2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < s1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < s2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [10,2,33,444,53,666]
print(arr)
print(Divide(arr,0,len(arr)-1))        