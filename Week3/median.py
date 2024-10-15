def median(data):
    if len(data) == 0:
        raise ValueError("No data")

    data.sort()
    if len(data) % 2 != 0:
        return data[len(data)//2]

    else:
        median = (data[len(data)//2 - 1] + data[len(data)//2])/2
        return int(median)
