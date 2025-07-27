with open("input.txt", "r") as f:
    octopus_lines = f.readlines()
octopus_grid = []
for line in octopus_lines:
    energy_row = []
    for energy_level in line.strip():
        energy_row.append(int(energy_level))
    octopus_grid.append(energy_row)
n = len(octopus_grid)
m = len(octopus_grid[0])

nbr_explosions = 0


def explode_octopus(
    i: int, j: int, grid: list[list[int]], exploded_cells: set[tuple[int, int]]
):
    exploded_cells.add((i, j))
    for row in range(max(i - 1, 0), min(i + 2, n)):
        for column in range(max(j - 1, 0), min(j + 2, m)):
            if row != i or column != j:
                grid[row][column] += 1
    for row in range(max(i - 1, 0), min(i + 2, n)):
        for column in range(max(j - 1, 0), min(j + 2, m)):
            if grid[row][column] >= 10 and (row, column) not in exploded_cells:
                explode_octopus(row, column, grid, exploded_cells)


def grid_to_str(grid: list[list[int]]):
    return "\n".join([" ".join([str(energy) for energy in line]) for line in grid])


print(grid_to_str(octopus_grid), end="\n\n\n")

for i in range(100):
    exploded_cells = set()
    for row in range(n):
        for column in range(m):
            octopus_grid[row][column] += 1
            if octopus_grid[row][column] >= 10 and (row, column) not in exploded_cells:
                explode_octopus(row, column, octopus_grid, exploded_cells)
    nbr_explosions += len(exploded_cells)
    for row, column in exploded_cells:
        octopus_grid[row][column] = 0
    print(
        grid_to_str(octopus_grid),
        end="\n\n\n",
    )

print(nbr_explosions)
