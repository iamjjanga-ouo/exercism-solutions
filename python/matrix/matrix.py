## Awesome Learning in this code
# 1. list comprehesion is more pythonic than general loop(init with empty list)
# 2. Make multi-line when list-comprehension is nested
class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
                        [int(element) for element in row.split()] # list(map(int, row.split()))
                        for row in matrix_string.split('\n')
                        ]
        # [[1,2],
        #  [3,4]]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]