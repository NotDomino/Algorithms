# Heap Sort Algorithm

def test(list = [5, 3, 8, 6, 7, 2]):
    print("Original list: ", list)
    print("Sorted list: ", heapSort(list))

def heapSort(list):
    # Convert list to heap
    length = len(list) - 1
    leastParent = length // 2

    for i in range(leastParent, -1, -1):
        moveDown(list, i, length)

    # Flatten heap into sorted array
    for i in range(length, 0, -1):
        if list[0] > list[i]:
            swap(list, 0, i)
            moveDown(list, 0, i - 1)

    return list

def moveDown(list, first, last):
    largest = 2 * first + 1
    
    while largest <= last:
        # Right child exists and is larger than left child
        if (largest < last) and (list[largest] < list[largest + 1]):
            largest += 1

        # Right child is larger than parent
        if list[largest] > list[first]:
            swap(list, largest, first)
            # Move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # Force exit
        
def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
