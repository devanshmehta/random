__author__ == 'devansh.mht@gmail.com'

def pow(x, y):
    if x == 0: 
        return 0
    if y == 0:
        return 1
    if y % 2 == 0:
        val = pow(x, y / 2)
        return val * val
    else:
        val = pow(x, (y - 1) / 2)
        return val * val * x
        
def pow_simple(x, y):
    if x == 0:
        return 0
    if y == 0:
        return 1
    mul = 1
    for i in xrange(y):
        mul *= x
    return mul
    
def main():
    print pow_simple(33, 180)
    
if __name__ == '__main__':
    main()
