#Insertion Sort
def insertionSort(a):
    no = len(a)
    for i in range(1, no):
        key = a[i]
        j = i - 1
        while(j>=0 and a[j] > key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a  

print(insertionSort([10, 44, 8, 5, 2, 66]))