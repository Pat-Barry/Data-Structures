# Method 1: using a nested loop -> time complexity = O(n^2)
def find_product1(lst):
    result = []
    temp = 1

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                temp *= lst[j]
        result.append(temp)
        temp = 1

    return result

# Optimizing the number of multiplications
def find_product2(lst):
    left = 1
    product = []

    for item in lst:
        product.append(left)
        left = left * item

    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product

lst = [1,2,3,4]
print(find_product2(lst))