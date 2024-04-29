#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                # Calculate the element using the Pascal's triangle formula
                element = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(element)
        triangle.append(current_row)

    return triangle

# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

