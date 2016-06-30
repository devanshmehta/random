# utility to find factors of given number

__author__ = 'devansh.mht@gmail.com'

def find_factors(num):
    '''Find the factors of the given num, if the num is negative 
       then factors of its absolute value is returned. Returns 
       list of tuple of factors. If the the number is prime then 
       empty list is returned.'''
    num = abs(num)
    low, high, factors = 1, num, []
    while True:
        if low > high:
            return factors
        if num % low == 0:
            high = num / low
            factors.append((low, high))
        low += 1
        high = num // low            

if __name__ == '__main__':
    print find_factors(3)
    print find_factors(100)
    print find_factors(32)
