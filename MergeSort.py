# Merge Sort Algorithm

def test(list=[5, 3, 8, 6, 7, 2]):
    print("Original list: ", list)
    mergeSort(list)
    print("Sorted list: ", list)

def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i += 1
            else:
                list[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j += 1
            k += 1
