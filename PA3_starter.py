#this is a starter code for Programming Assignment 3.


def swap(arr, i, j) -> None:
    """ Takes and array and swaps the 
        values at index i and j
    """
    #arr[i], arr[j] = arr[j], arr[i]
    temp = arr[i]  
    arr[i] = arr[j]  
    arr[j] = temp

def selection_sort(values: list[int]) -> None:
    counts = {
            "data_comparisons": 0,
            "loop_comparisons": 0,
            "data_assignments": 0,
            "loop_assignments": 0,
            "other": 0 
            }

    
    i = 0
    counts["loop_assignments"] += 1
    while i < len(values) - 1:
        counts["loop_comparisons"] += 1
        min_index = i
        counts["data_assignments"] += 1
        j = i + 1
        counts["loop_assignments"] += 1
        while j < len(values):
            counts["loop_assignments"] += 1
            counts["data_comparisons"] += 1
            if values[j] < values[min_index]:
                # TODO: Update min_index.
                min_index = j
            j += 1
        counts["loop_comparisons"] += 1
        #keeping track exit while loop
        # TODO:
        # if current i is the minimum value, do nothing
        # if not, swap items i and min_index
        # count the operations it takes to do these
        counts["other"] += 1
        if min_index != i:
            swap(values, i, min_index)
            counts["data_assignments"] += 3

        i += 1
        print(f"i: {i}, j: {j}, min_index: {min_index}, values: {values}")
    counts["loop_comparisons"] += 1
    return counts



def main():
    l = [1,8,5,2,4,9,0]
    counts = selection_sort(l)
    print(l)
    print(counts)

if __name__=="__main__":
    main()