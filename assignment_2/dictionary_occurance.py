def count_occurrences(numbers):
    freq = {}  

    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# Testing with 3 different lists
list1 = [1, 2, 2, 3, 1, 4]
list2 = [5, 5, 5, 6]
list3 = [7, 8, 9, 7, 8, 7]

print("List 1:", count_occurrences(list1))
print("List 2:", count_occurrences(list2))
print("List 3:", count_occurrences(list3))