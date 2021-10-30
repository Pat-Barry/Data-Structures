# Method 1: Brute force approach. Tinme Complexity = O(n^2)
def find_sum1(lst,k):
    if len(lst) == 0 or len(lst) == 1:
        return -1

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i is not j and lst[i] + lst[j] == k:
                return [lst[i],lst[j]]
    return -1

# Method 2: Sorting the list. Time Complexity = 0(nlogn)
def binary_search(A, item):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == item:
            return mid
        elif A[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def find_sum2(lst, k):
    lst.sort()
    for i in range(len(lst)):
        index = binary_search(lst, k - lst[i])
        if index != -1 and index != i:
            return [lst[i], k - lst[i]]
    return -1






lst = [1,4,7,9,10]
k = 13

print(binary_search(lst, 4))
print(find_sum2(lst, k))