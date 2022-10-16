def sum1(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + sum1(arr)


print(sum1([2, 4, 6]))
