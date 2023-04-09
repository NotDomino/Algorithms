# Selection Sort Algorithm

def test(list = [5, 3, 8, 6, 7, 2]):

    print("Original list: ", list)
    selectionSort(list)
    print("Sorted list: ", list)


def selectionSort(list):
    for i in range(len(list)):
        min = i

        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp
