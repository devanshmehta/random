__author__ = 'devansh.mht@gmail.com'

# utility to find number of inversions in an array
# https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)

def _get_mid(low, high):
    return low + (high - low) // 2

def _merge_and_count_inversion(low, high, arr, tmp):
    num_inversions = 0
    mid = _get_mid(low, high)
    l_pointer = mid
    r_pointer = high
    tmp_pointer = high
    while l_pointer >= low and r_pointer >= mid + 1:
        if arr[l_pointer] > arr[r_pointer]:
            tmp[tmp_pointer] = arr[l_pointer]
            num_inversions += r_pointer - mid
            tmp_pointer -= 1
            l_pointer -= 1
        else:
            tmp[tmp_pointer] = arr[r_pointer]
            tmp_pointer -= 1
            r_pointer -= 1
    while l_pointer >= low:
        tmp[tmp_pointer] = arr[l_pointer]
        tmp_pointer -= 1
        l_pointer -= 1
    while r_pointer >= mid + 1:
        tmp[tmp_pointer] = arr[r_pointer]
        tmp_pointer -= 1
        r_pointer -= 1
    for i in xrange(low, high + 1):
        arr[i] = tmp[i]
    return num_inversions

def _divide_and_merge(low, high, arr, tmp):
    if low >= high:
        return 0
    mid = _get_mid(low, high)
    inversions =  _divide_and_merge(low, mid, arr, tmp)
    inversions += _divide_and_merge(mid + 1, high, arr, tmp)
    inversions += _merge_and_count_inversion(low, high, arr, tmp)
    return inversions

def count_inversions(arr):
    tmp = [-1] * len(arr)
    return _divide_and_merge(0, len(arr) - 1, arr, tmp)

if __name__ == '__main__':
    arr = [4,1,5,2,6,3]
    print count_inversions(arr)
    
