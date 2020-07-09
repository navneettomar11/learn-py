from typing import List


def number_of_neighbour(grid, r, c, n, m) -> int:
    count = 0
    if r > 0 and grid[r - 1][c]:  # UP
        count += 1
    if r < n - 1 and grid[r + 1][c]:  # DOWN
        count += 1

    if c > 0 and grid[r][c - 1]:  # LEFT
        count += 1

    if c < m - 1 and grid[r][c + 1]:  # RIGHT
        count += 1
    return count


def islandPerimeter(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    def sum_adjacent(i, j):
        adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
        res = 0
        print(adjacent, '--> ', i, j)
        for x, y in adjacent:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                res += 1
        return res

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += sum_adjacent(i, j)
    return count


if __name__ == "__main__":
    print(islandPerimeter([[0, 1, 0, 0],
                           [1, 1, 1, 0],
                           [0, 1, 0, 0],
                           [1, 1, 0, 0]]
                          ))
    """
    print(islandPerimeter([[0, 0, 0, 0],
                           [1, 1, 1, 0],
                           [0, 1, 0, 0],
                           [1, 0, 0, 0]]
                          ))

    print(islandPerimeter([[1]]))

    print(islandPerimeter([[0,1]]))
    """
