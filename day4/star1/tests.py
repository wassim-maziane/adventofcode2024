from solution import diagonals_matrice
from solution import transpose_matrice, diagonals_matrice, anti_diagonals_matrice

matrice = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
    ["9", "10", "11", "12"],
    ["13", "14", "15", "16"],
]
lines = matrice
print("lines :")
print(lines)
reversed_lines = [line[::-1] for line in lines]
print("reversed_lines :")
print(reversed_lines)
columns = transpose_matrice(matrice)
print("columns :")
print(columns)
reversed_columns = [column[::-1] for column in columns]
print("reversed_columns :")
print(reversed_columns)
diagonals = diagonals_matrice(matrice)
print("diagonals :")
print(diagonals)
reversed_diagonals = [diagonal[::-1] for diagonal in diagonals]
print("reversed_diagonals :")
print(reversed_diagonals)
anti_diagonals = anti_diagonals_matrice(matrice)
print("anti_diagonals :")
print(anti_diagonals)
reversed_anti_diagonals = [anti_diagonal[::-1] for anti_diagonal in anti_diagonals]
print("reversed_anti_diagonals :")
print(reversed_anti_diagonals)
