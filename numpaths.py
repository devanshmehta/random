# utility to find number of paths from src to destination

def num_paths(src, dest, grid, dp):
    if src == dest:
        return 1
    if dp[src[0]][src[1]] != -1:
        # check if we have available in cache
        return dp[src[0]][src[1]]
    else:
        # find the number of paths and put it in cache 
        # for later use
        count = 0
        if src[0] + 1 < len(grid):
            count += num_paths((src[0] + 1, src[1]), dest, grid, dp)
        if src[1] + 1 < len(grid[0]):
            count += num_paths((src[0], src[1] + 1), dest, grid, dp)
        dp[src[0]][src[1]] = count
        return count
    
if __name__ == '__main__':
    src = (0, 0)
    dest = (2, 2)
    grid = [[0] * 3] * 3
    dp = []
    for i in grid:
        row = [-1] * 3
        dp.append(row)
    print num_paths(src, dest, grid, dp)
            
