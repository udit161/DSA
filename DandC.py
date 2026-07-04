def find_min__max(arr, start, end):
    if(start == end):
        return arr[start],arr[end]

    if(start + 1 == end):
        if(arr[start] < arr[end]):
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
    
    mid = (start + end) // 2
    min1,max1 = find_min__max(arr, start, mid)
    min2,max2 = find_min__max(arr, mid+1, end)
    
    if(min1<min2):
        minval = min1
    else:
        minval = min2
    
    if(max1>max2):
        maxval = max1
    else:
        maxval = max2
    
    return minval,maxval
    
arr = [10,2,33,444,53,666]
print(find_min__max(arr,0,len(arr)-1))    
    