# Program to Demonstrate Column-Major Order Representation of a 2D Array

def column_major_index(row, col, num_rows):
    return col * num_rows + row

print("=== Column-Major Order Representation ===")

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

print("\nColumn-Major (Linear) Representation:")
linear = []
for j in range(cols):
    for i in range(rows):
        linear.append(matrix[i][j])
print(linear)

print("\nIndex Mapping (Column-Major):")
for j in range(cols):
    for i in range(rows):
        idx = column_major_index(i, j, rows)
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}  -->  linear[{idx}]")


