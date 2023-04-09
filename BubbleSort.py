#simple bubble sort algorithm

def test(list = [5, 3, 8, 6, 7, 2]):

    print("Original list: ", list)
    bubbleSort(list)
    print("Sorted list: ", list)

def bubbleSort(list):
    #loop through the list
    for i in range(len(list)):
        
        #loop through the list again
        for j in range(len(list)):
            #compare the elements
            
            if list[i] < list[j]:
                #swap the elements
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
