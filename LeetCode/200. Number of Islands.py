import random

def numIsland(grid, n, m):
    count = 0
    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                count += 1
                clearRestOfLand(grid, j, i)
    return count
def clearRestOfLand(grid, j, i):
    if j < 0 or i < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return

    grid[i][j] = 0
    clearRestOfLand(grid, j + 1, i)
    clearRestOfLand(grid, j - 1, i)
    clearRestOfLand(grid, j, i - 1)
    clearRestOfLand(grid, j, i + 1)


m = int(input('Enter length of grid: '))
n = int(input('Enter height of grid: '))

grid = [[int(random.randint(0, 1)) for j in range(n)] for i in range(m)]
print('Your m x n 2D binary grid: ', '')
for j in range(n):
    for i in range(m):
        print(grid[i][j], end=' ')
    print('')

print('Number of islands: ', numIsland(grid, n, m))


