# Insertion Sort Algorithm

def test(list = [5, 3, 8, 6, 7, 2]):

    print("Original list: ", list)
    insertionSort(list)
    print("Sorted list: ", list)

def insertionSort(list):
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index
        
        while (position>0) and (list[position-1]>currentvalue):
            list[position]=list[position-1]
            position = position-1

        list[position]=currentvalue