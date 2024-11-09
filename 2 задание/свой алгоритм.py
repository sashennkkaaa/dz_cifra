import random
import time
def shaker(array): 
    size = 10000 
    swapped = True
    StartInd = 0
    EndInd = size - 1
    while (swapped == True): 
        swapped = False
        for i in range(StartInd, EndInd): 
            if (array[i] > array[i + 1]) : 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
        if (not(swapped)): 
            break
        swapped = False
        EndInd = EndInd - 1
        for i in range(EndInd - 1, StartInd - 1, -1): 
            if (array[i] > array[i + 1]): 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
        StartInd = StartInd + 1
start_time = time.time()
arr = [random.randint(1, 10000) for _ in range(10000)]
shaker(arr) 
print("--- %s seconds ---" % (time.time() - start_time))
