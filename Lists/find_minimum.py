# Method 1: sorting the list. Time complexity = O(nlogn)
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

            k += 1
        
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        

def find_minimum1(lst):
    if len(lst) == 0:
        return None

    merge_sort(lst)
    return lst[0]

def find_minimum2(lst):
    min = lst[0]
    for item in lst:
        if item < min:
            min = item
    return min

lst = [2,-200,5,6,-7,8,9,3,2]


print(find_minimum2(lst))