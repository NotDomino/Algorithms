#Quick Sort Algorithm

def test(list = [5, 3, 8, 6, 7, 2]):
    print("Original list: ", list)
    print("Sorted list: ", quickSort(list))


def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
        items_greater = []
        items_lower = []

        for item in list:
            if item > pivot:
                items_greater.append(item)

            else:
                items_lower.append(item)

        return quickSort(items_lower) + [pivot] + quickSort(items_greater)
