#Max_min diff
def Max_min_diff(arr):
    arr.sort()
    n=len(arr)
    min_diff = float('inf')
    max_diff = float('-inf')

    for i in range(n-1):
        diff = abs(arr[i+1]-arr[i])
        if diff<min_diff:
            min_diff = diff
        if diff>max_diff:
            max_diff = diff

    return min_diff,max_diff

print(Max_min_diff([10,2,33,444,53,666]))