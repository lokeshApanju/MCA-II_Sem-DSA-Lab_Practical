# Program to Demonstrate Row-Major Order Representation of a 2D Array

def row_major_index(row, col, num_cols):
    return row * num_cols + col


print("=== Row-Major Order Representation ===")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


matrix = []
print("Enter matrix elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"  Element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

print("\nMatrix:")
for row in matrix:
    print(row)

print("\nRow-Major (Linear) Representation:")
linear = []
for i in range(rows):
    for j in range(cols):
        linear.append(matrix[i][j])
print(linear)


print("\nIndex Mapping (Row-Major):")
for i in range(rows):
    for j in range(cols):
        idx = row_major_index(i, j, cols)
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}  -->  linear[{idx}]")

