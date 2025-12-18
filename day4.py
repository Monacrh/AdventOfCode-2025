# grid = [list(input().rstrip()) for _ in range(138)]

# rows = len(grid)
# cols = len(grid[0])
# print(rows, cols)

# directions = [
#     (-1, -1), (-1, 0), (-1, 1),
#     ( 0, -1),          ( 0, 1),
#     ( 1, -1), ( 1, 0), ( 1, 1)
# ]

# total = 0

# for i in range(rows):
#     for j in range(cols):
#         if grid[i][j] != '@':
#             continue

#         count = 0
#         for dr, dc in directions:
#             ni, nj = i + dr, j + dc
#             if 0 <= ni < rows and 0 <= nj < cols:
#                 if grid[ni][nj] == '@':
#                     count += 1

#         if count < 4:
#             total += 1

# print(total)

#Part 2
grid = [list(input().strip()) for _ in range(138)]

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def accessible(grid, r, c):
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    return count < 4

total_removed = 0

while True:
    to_remove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and accessible(grid, r, c):
                to_remove.append((r, c))

    if not to_remove:
        break

    for r, c in to_remove:
        grid[r][c] = '.'

    total_removed += len(to_remove)

print(total_removed)
