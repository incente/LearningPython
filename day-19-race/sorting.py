def selection_sort_copy(arr):
    arr_copy = arr[:]

    for i in range(len(arr_copy)):
        min_index = i
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j
        
        arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]
    
    return arr_copy
