def less_than(original, n):
    new_list = []           # Make a new, empty list
    for i in range(0, len(original)):  # Every integer in "original" list
        if original[i] < n:
            new_list.append(original[i])
    return new_list


# Example
list = [5, 67, 1, 457, 21, 3, 67, 11, 10, 22, 34]
n = 30

print("Original list: ", list)
print(f"New list (Less than {n}): ", less_than(list, n))
