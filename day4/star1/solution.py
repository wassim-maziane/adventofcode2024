def transpose_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(i + 1, len(matrice[0])):
            matrice[i][j], matrice[j][i] = matrice[j][i], matrice[i][j]
    return matrice


def diagonals_matrice(matrice):
    n = len(matrice)
    m = len(matrice[0])
    main_diagonal = [matrice[i][i] for i in range(min(n, m))]
    diagonals = [main_diagonal]
    for i in range(1, n):
        diagonal = [matrice[i + j][j] for j in range(min(n - i, m))]
        diagonals.append(diagonal)
    for j in range(1, m):
        diagonal = [matrice[i][i + j] for i in range(min(m - j, n))]
        diagonals.append(diagonal)
    return diagonals


def anti_diagonals_matrice(matrice):
    n = len(matrice)
    m = len(matrice[0])
    anti_diagonals = []
    for i in range(1, n):
        anti_diagonal = [matrice[i - j][j] for j in range(min(i + 1, m))]
        anti_diagonals.append(anti_diagonal)
    for j in range(1, m):
        anti_diagonal = [matrice[n - i - 1][j + i] for i in range(min(n, m - j))]
        anti_diagonals.append(anti_diagonal)
    return anti_diagonals


def check_matrice(matrice):
    lines = matrice
    reversed_lines = [line[::-1] for line in lines]
    columns = transpose_matrice(matrice)
    reversed_columns = [column[::-1] for column in columns]
    diagonals = diagonals_matrice(matrice)
    reversed_diagonals = [diagonal[::-1] for diagonal in diagonals]
    anti_diagonals = anti_diagonals_matrice(matrice)
    reversed_anti_diagonals = [anti_diagonal[::-1] for anti_diagonal in anti_diagonals]
    lines_to_check = (
        lines
        + reversed_lines
        + columns
        + reversed_columns
        + diagonals
        + reversed_diagonals
        + anti_diagonals
        + reversed_anti_diagonals
    )
    xmas_count = 0
    print(lines_to_check, len(lines_to_check))
    for line in lines_to_check:
        xmas_count += check_line(line)
    return xmas_count


def check_line(line):
    xmas_count = 0
    for i in range(len(line) - 3):
        if line[i : i + 4] == ["X", "M", "A", "S"]:
            xmas_count += 1
    return xmas_count


if __name__ == "__main__":
    matrice = []
    with open("sample.txt", "r") as f:
        for line in f:
            matrice.append(list(line[:-1]))
    print(check_matrice(matrice))
    print(matrice)
