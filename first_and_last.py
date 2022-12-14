def last(arr):
    if isinstance(arr, list) and len(arr) != 0:
        return arr[-1]
    else: return 'none'

def first(arr):
    if isinstance(arr, list) and len(arr) != 0:
        return arr[0]
    else: return 'none'
