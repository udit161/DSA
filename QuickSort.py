def QuickSort(arr , l, r):
    if(l < r):
        p = partition(arr, l, r)
        QuickSort(arr, l, p-1)
        QuickSort(arr, p+1, r)
    return arr


def partition(arr , l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l,r): 
        if(arr[j]<= pivot):
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
    
    arr[i+1],arr[r] = arr[r], arr[i+1]
    return i+1

arr = [10,2,33,444,53,666]
print(arr)
print(QuickSort(arr,0,len(arr)-1))        