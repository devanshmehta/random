import random, time

def check_sorted(l):
    '''checks if the list is sorted. Returns True
       if it is sorted otherwise false'''
    prev = -1
    for i in l:
        if prev > i:
            return False
        else:
            prev = i
    return True

def insertion_sort(unsorted_list):
    '''sorts the unsorted_list and returns it'''
    l_size = len(unsorted_list)
    for i in xrange(1, l_size):
        num = unsorted_list[i]
        for j in xrange(i - 1, -1, -1):
            if unsorted_list[j] <= num:
                unsorted_list[j + 1] = num
                break
            else:
                unsorted_list[j + 1] = unsorted_list[j]
                unsorted_list[j] = num
    return unsorted_list

def bubble_sort(unsorted_list):
    '''sorts the unsorted list and returns list'''
    pass

def merge_sort(unsorted_list):
    def merge(l_arr, r_arr):
        '''merge 2 sorted arrays and returns the merged array'''
        n_arr = []
        l_pointer = 0
        r_pointer = 0
        while l_pointer < len(l_arr) and r_pointer < len(r_arr):
            if l_arr[l_pointer] <= r_arr[r_pointer]:
                n_arr.append(l_arr[l_pointer])
                l_pointer += 1
            else:
                n_arr.append(r_arr[r_pointer])
                r_pointer += 1
        while l_pointer <len(l_arr):
            n_arr.append(l_arr[l_pointer])
            l_pointer += 1
        while r_pointer < len(r_arr):
            n_arr.append(r_arr[r_pointer])
            r_pointer += 1
        return n_arr

    def sort(l, r, unsorted_list):
        if l < r:
            mid = (r + l) / 2
            l_arr = sort(l, mid, unsorted_list)
            r_arr = sort(mid + 1, r, unsorted_list)
            return merge(l_arr, r_arr)
        else:
            return [unsorted_list[l]]

    return sort(0, len(unsorted_list) - 1, unsorted_list)

def quick_sort(unsorted_list):
    def partition(start, end, arr):
        '''partitions the subarray between start and end using start 
           as pivot and returns the index of left subarray'''
        if start == end:
            return start
        pivot = arr[start]
        l = start - 1
        r = end + 1
        while True:
            l += 1
            while l < end and arr[l] < pivot:
                l += 1
            r -= 1
            while r > start and arr[r] > pivot:
                r -= 1
            if l < r:
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
            else:
                return r
    def qsort(start, end, arr):
        if start >= end:
            return
        else:
            l_index = partition(start, end, arr)
            qsort(start, l_index, arr)
            qsort(l_index + 1, end, arr)
    qsort(0, len(unsorted_list) - 1, unsorted_list)    
    return unsorted_list

def heap_sort(unsorted_list):
    pass

def main():
    l = [i for i in range(0, 100000, 1)]
    random.shuffle(l)
    print check_sorted(l)
    print "start"
    
    start = time.time()  
    copy = l [:]
    s_l = insertion_sort(copy)
    end = time.time()
    print end - start
    print check_sorted(s_l)

    start = time.time()    
    s_l = merge_sort(l)
    end = time.time()
    print end - start
    print check_sorted(s_l)
    
    start = time.time()    
    s_l = quick_sort(l)
    end = time.time()
    print end - start
    print check_sorted(s_l)
    

if __name__ == '__main__':
    main()

    
