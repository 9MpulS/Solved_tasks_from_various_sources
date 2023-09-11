import random

m = int(input('Enter length of grid: '))    # enter length and height
n = int(input('Enter height of grid: '))

grid = [[int(random.randint(0, 1)) for j in range(n)] for i in range(m)]

print('Your m x n 2D binary grid: ', '')    # print random grid
for j in range(n):
    for i in range(m):
        print(grid[i][j], end=' ')
    print('')

def numIsland(grid, n, m):  # function to count the number of islands
    count = 0
    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                count += 1
                clearRestOfLand(grid, j, i)
    return count
def clearRestOfLand(grid, j, i):    # function to depth-first search
    if j < 0 or i < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return

    grid[i][j] = 0  # mark the current land as visited
    clearRestOfLand(grid, j + 1, i) # explore adjacent lands
    clearRestOfLand(grid, j - 1, i)
    clearRestOfLand(grid, j, i - 1)
    clearRestOfLand(grid, j, i + 1)

print('Number of islands: ', numIsland(grid, n, m))
