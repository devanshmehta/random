def rsearch(l, val, lo = 0, high = None):
    """returns the right most index of val if val 
       is in the l otherwise returns index x such that 
       l[x] >= val and l[x - 1] < val"""
    if not high:
        high = len(l) - 1
    while lo < high:
        mid = (lo + high) // 2
        if l[mid] > val:
            high = mid
        elif l[mid] < val:
            lo = mid + 1
        else:
            if l[mid + 1] == val:
                lo = mid + 1
            else:
                return mid
    return lo        

