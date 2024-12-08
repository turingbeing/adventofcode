def find_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [
        # right, down, diagonal down-right, diagonal up-right
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1),
    ]
    xmas_positions = []

    def check_xmas(r, c, dr, dc):
        word = ""
        positions = []

        for i in range(4):
            if 0 <= r < rows and 0 <= c < cols:
                word += grid[r][c]
                positions.append((r, c))
                if i == 3:
                    if word == "XMAS":
                        xmas_positions.extend(positions)
                    elif word == "SAMX":
                        xmas_positions.extend(positions[::-1])
                r += dr
                c += dc
            else:
                return

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                check_xmas(r, c, dr, dc)

    return xmas_positions


def find_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    x_mas_count = 0

    def check_x_mas(r, c):
        patterns = [
            # Center, Top-left, Top-right, Bottom-left, Bottom-right
            [(0, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)],
        ]

        for pattern in patterns:
            mas_positions = []
            for dr, dc in pattern:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    mas_positions.append(grid[nr][nc])
                else:
                    break
            else:
                center, tl, tr, bl, br = mas_positions
                if center == "A":
                    if ((tl == "M" and br == "S") or (tl == "S" and br == "M")) and (
                        (tr == "M" and bl == "S") or (tr == "S" and bl == "M")
                    ):
                        return 1
        return 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            x_mas_count += check_x_mas(r, c)

    return x_mas_count


def create_grid(grid, xmas_positions):
    output = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for r, c in xmas_positions:
        output[r][c] = grid[r][c]
    return ["".join(row) for row in output]


with open("files/input.txt", "r") as file:
    grid = [line.strip() for line in file]

xmas_positions = find_xmas(grid)
output = create_grid(grid, xmas_positions)

for row in output:
    print(row)

x_mas_positions = find_x_mas(grid)
# output = create_grid(grid, x_mas_positions)


print(f"\nNumber of XMAS occurences: {len(xmas_positions) // 4}")
print(f"Number of X-MAS occurences: {x_mas_positions}")
