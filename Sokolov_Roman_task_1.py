matrix_1 = [[5, 25, 6],
            [6, 68, 78],
            [45, 57, 87]
            ]
matrix_2 = [[5, 25, 6],
            [6, 68, 78],
            [45, 57, 87]
            ]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{" ".join(str(elem) for elem in self.matrix[0])}\n' \
               f'{" ".join(str(elem) for elem in self.matrix[1])}\n' \
               f'{" ".join(str(elem) for elem in self.matrix[2])}'

    def __add__(self, other):
        return [
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matrix, other.matrix)
        ]


m1 = Matrix(matrix_1)
print(m1)
m2 = Matrix(matrix_2)
m3 = (m1 + m2)
print(m3)
