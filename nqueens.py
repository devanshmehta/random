'''counting all the solutions in the n queens problem.
   The solution is based on niklaus wirth's solution
   for 8 queens board
'''
___author__ = 'devansh.mht@gmail.com'

class Board(object):
    '''board class to be userd for blocking and unblocking'''
    
    def __init__(self, n):
        self.n = n
        self.rows = [True] * n
        self.sum_diag = [True] * ((n * 2) - 1)
        self.diff_diag = [True] * ((n * 2) - 1)
    
    def block_board(self, i, j):
        self.rows[i] = False
        self.sum_diag[i + j] = False
        self.diff_diag[i - j + (self.n - 1)] = False

    def unblock_board(self, i, j):
        self.rows[i] = True
        self.sum_diag[i + j] = True
        self.diff_diag[i - j + (self.n - 1)] = True
        
    def safe_square(self, i, j):
        return (self.rows[i] and self.sum_diag[i + j] and 
                self.diff_diag[i - j + (self.n - 1)])

def count_queens_starting_at(row, column, board):
    count = 0
    if column >= board.n:
	return 1
    for i in xrange(row, board.n):
        if not board.safe_square(i, column):	
             continue
        board.block_board(i, column)
        count += count_queens_starting_at(0, column + 1, board)
        board.unblock_board(i, column)
    return count
    
def count_queens(n):
    board = Board(n)
    count = count_queens_starting_at(0, 0, board)
    return count
    
def main():
    n = int(raw_input())
    print count_queens(n)

if __name__ == '__main__':
    main()
