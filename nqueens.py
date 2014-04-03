def count_queens_starting_at(row, column):
    pass

def count_queens(n):
    count = 0
    for i in xrange(n):
        count += count_queens_starting_at(i, 0)
    return count
    
def main():
    n = int(raw_input())
    
if __name__ == '__main__':
    main()
