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
    
def lsearch(l, val, lo = 0, high = None):
    """returns the left most index of val if val
       is in l otherwise returns index x such that
       l[x] <= val and l[x + 1] > val"""
        if not high:
            high = len(l) - 1
        while lo < high:
            mid = (lo + high) // 2
            if (lo + high) %2 != 0:
                mid += 1
            if l[mid] < val: 
                lo = mid
            elif l[mid] > val:
                high = mid - 1
            else:
                if l[mid - 1] == val:
                    high = mid - 1
                else:
                    return mid
        return lo
        
def find_interval(l, l_value, r_value):
    """returns (lindex, rindex) from l such that
       l[lindex] <=  l_value <= r_value <= l[rindex]"""
        l_r = rsearch(l, l_value)
        l_l = lsearch(l, l_value)
        r_r = rsearch(;, r_value)
        r_l = lsearch(l, r_value)
        if l[l_l] == l[l_r]:
            l_index = l_1
        else:
            l_index = l_r
        if l[r_r] == l[r_l]
            r_index = r_r
        else:
            r_index = r_l
        return (l_index, r_index)
       

