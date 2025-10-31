'''
Bubble sort, Insertion sort, Selection sort
Efficient sorts: Merge sort, Quick sort, Heap sort
Bucket sort, Radix sort
'''

from Heap import MinHeap

def bubbleSort(array): # O(n^2)
    length = len(array)
    for i in range(length):
        isSwap = False
        for j in range(length-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                isSwap = True
        if not isSwap: break
        disp(array)

def insertionSort(array): # O(n^2)
    length = len(array)
    for i in range(1, length):
        temp = array[i]
        j = i - 1
        while(j>=0 and array[j] > temp):
            array[j+1]  = array[j]
            j -= 1
        array[j+1] = temp
        # disp(array)


def selectionSort(array):
    length = len(array)
    for i in range(length-1, -1, -1):
        maxIdx = i
        for j in range(i):
            if array[maxIdx] < array[j]: maxIdx = j
        array[maxIdx], array[i] = array[i], array[maxIdx]
        disp(array)

def quickSort(array):
    length = len(array)
    fIdx = 0
    lIdx = length - 1
    quickSort_(array, fIdx, lIdx)
    disp(array)

def quickSort_(array, fIdx, lIdx):
    pivot = lIdx
    current = fIdx
    swapMarker = fIdx-1
    if fIdx >= lIdx: return
    for current in range(fIdx, lIdx + 1):
        if array[current] <= array[pivot]:
            swapMarker += 1
            if current > swapMarker:
                array[current], array[swapMarker] = array[swapMarker], array[current]
    pivot = swapMarker
    

    quickSort_(array, fIdx, pivot-1)
    quickSort_(array, pivot+1, lIdx)

# def mergeSort(array):


def mergeSort_(array):
    mIdx = len(array) // 2
   
    disp(array)

    if len(array) <= 1: return
    mergeSort_(L)
    mergeSort_(R)
    
    # merge
    i, j, k = 0, 0, 0
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i<len(L):
        array[k] = L[i]
        i += 1
        k += 1

    while j<len(R):
        array[k] = R[j]
        j += 1
        k += 1
    
    disp(array)


def heapSort(array):
    length = len(array)
    mH = MinHeap(length)
    # reconstruct array to min heap
    for i in range(length):
        mH.insert(array[i])
    # sort
    for i in range(length):
        array[i] = mH.arrayNodes[0].data
        mH.delete(array[i])
        print(f"loop {i}: {array}")

    # disp(array)

def bucketSort(array):
    length = len(array)
    nBuckets = 3
    # buckets = [[], [], []]
    buckets = [[] for i in range(nBuckets)]
    # distribute array to buckets
    for i in range(length):
        if array[i] <= 3:
            buckets[0].append(array[i])
        elif array[i] <= 6:
            buckets[1].append(array[i])
        else:
            buckets[2].append(array[i])
    # sort each bucket
    for i in range(nBuckets):
        insertionSort(buckets[i])
    # merge buckets
    array = []
    for i in range(nBuckets):
        array += buckets[i]
    
    print(array)

def radixSort(array):
    length = len(array)
    nLoops = maxDigitNumber(array)
    base = 1
    for i in range(nLoops):
        nLists = [[] for i in range(10)]
        for j in range(length):
            idx = (array[j] // base) % 10
            nLists[idx].append(array[j])
        base *= 10

        array = []
        for k in range(10):
            array += nLists[k]

    print(array)

def maxDigitNumber(array):
    m = max(array)
    return len(str(m))

def disp(array):
    for i in range(len(array)):
        print(array[i], end = "  ")
    print()

# array = [3, 7, 9, 10, 2, 6, 1, 4, 8, 5]
array = [24, 320, 672, 318, 1200, 654, 910, 78, 76]
print(array)
# print("buuble sort")
# bubbleSort(array)
# insertionSort(array)
# selectionSort(array)
# quickSort(array)
# mergeSort_(array)
# print("heap sort")
# heapSort(array)
# print("bucket sort")
# bucketSort(array)
print("radix sort")
radixSort(array)
