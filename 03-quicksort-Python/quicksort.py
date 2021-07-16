"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if (len(array) < 2):
        return array
    else:
        first = array[0]  # pivot
        rest = array[1:]
        lo = [x for x in rest if x < first]
        hi = [x for x in rest if x >= first]
        return quicksort(lo) + [first] + quicksort(hi)
