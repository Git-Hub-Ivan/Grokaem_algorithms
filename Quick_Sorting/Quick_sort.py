from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        randindex = randint(0, len(array) - 1)
        pivot = array[randindex]
        less = [i for i in array[:randindex]+array[randindex+1:] if i <= pivot]
        greater = [i for i in array[:randindex]+array[randindex+1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([4, 3, 6, 1, 66, 12]))
