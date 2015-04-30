import random

def fisherAlgo(nums, size):
    length = len(nums)
    for i in xrange(size):
        x = random.randint(0, length - 1)
        tmp = nums[x]
        nums[x] = nums[length - 1]
        nums[length - 1] = tmp
        length -= 1

def endlessAlgo(nums, size):
    randm = {}
    length = len(nums)
    while len(randm) < size:
       x = random.randint(0, length - 1)
       randm[x] = ''

def main():
    import time
    nums = range(1000000)
    start = time.clock()
    fisherAlgo(nums, 1000000)
    stop = time.clock()
    print stop - start
    start = time.clock()
    endlessAlgo(nums, 1000000)
    stop = time.clock()
    print stop - start

if __name__ == '__main__':
    main()
