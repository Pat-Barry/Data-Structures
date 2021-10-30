#Method 1: Creating a new list. Time complexity = O(n+m).
def merge_list1(l1,l2):
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(l1) + len(l2)):
        result.append(i)

    while (index_arr1 < len(l1) and index_arr2 < len(l2)):
        if (l1[index_arr1] < l2[index_arr2]):
            result[index_result] = l1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = l2[index_arr2]
            index_result += 1
            index_arr2 += 1

    while (index_arr1 < len(l1)):
        result[index_result] = l1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while (index_arr2 < len(l2)):
        result[index_result] = l2[index_arr2]
        index_result += 1
        index_arr2 += 1

    return result
#Method 2: Merging in place. Time complexity = O(mn) BUT space complexity is O(m)
def merge_list2(l1, l2):
    index1 = 0
    index2 = 0
    
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] > l2[index2]:
            l1.insert(index1,l2[index2])
            index1 += 1
            index2 += 1
        else:
            index1 += 1
    
    if index2 < len(l2):
        l1.extend(l2[index2:])
    return l1

l1 = [1,3,5,7]
l2 = [2,4,6,8]

combined = merge_list2(l1,l2)
print(combined)
