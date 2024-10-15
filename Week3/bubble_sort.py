def bubble_sort(lst):
    if not isinstance(lst, list):
        raise ValueError("Please insert list")

    if len(lst) < 2:
        return lst

    for i in range(len(lst), 1, -1):
        for j in range(i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst
