lst1 = [61, 17, 173, -138, -72, -26, -17, 141, -188, -150, 40, 44, -60, 95, 76, 190, -175, -111, -164, 46, 58, 112, 69, 171, 114, -158, -151, 159, 4, 84, 32, -165, 134, -110, 86, -34, -194]
lst2 = lst1
def remove_evens1(lst):
    odds = []
    for item in lst:
        if item % 2 != 0:
            odds.append(item)
    return odds

print (remove_evens1(lst1))

# remove_evens1 has a time complexity of O(n)

def remove_evens2(lst):
    return [number for number in lst if number % 2  != 0]

print(remove_evens2(lst2))

# remove_evens2 has a time complexity of O(n)