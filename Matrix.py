import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matarr = matrix

    def __getitem__(self, item):
        return self.matarr

    def __setitem__(self, key, value):
        self.matarr[key] = value

    @classmethod
    def same_values_on_diagonal(cls, width, height, diagonals_vector, diagonal_start):
        if not isinstance(diagonals_vector, list):
            return "wrong parameters"
        diag = 0
        vector = [0] * width
        tab = []
        scope = range(diagonal_start, diagonal_start + len(diagonals_vector))
        for _ in range(height):
            for i in scope:
                if 0 <= diag + i < width:
                    vector[diag + i] = diagonals_vector[i - diagonal_start]
            tab += vector
            for i in scope:
                if 0 <= diag + i < width:
                    vector[diag + i] = 0
            diag += 1
        return Matrix(np.array(tab, dtype=float).reshape(height, width))

    @classmethod
    def identity_matrix(cls, size):
        return Matrix.same_values_on_diagonal(size, size, [1], 0)

    def get_heigth(self):
        return self.matarr.shape[0]

    def get_width(self):
        return self.matarr.shape[1]

    def multiply_by_vector(self, vector):
        if not isinstance(vector, list):
            return "wrong parameters"
        if self.get_width() != len(vector):
            return []
        vec = [0] * self.get_heigth()
        for i in range(self.get_heigth()):
            for n in range(self.get_width()):
                vec[i] += vector[n] * self.matarr[i, n]
        return vec

    def multiply_by_matrix(self, matrix):
        if not isinstance(matrix, Matrix):
            return "wrong parameters"
        if self.get_width() != matrix.get_heigth() or self.get_heigth() != matrix.get_width():
            return []
        table = [0] * pow(self.get_heigth(), 2)
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for w in range(self.get_heigth()):
            for h in range(self.get_heigth()):
                for n in range(self.get_width()):
                    mat[h, w] += self.matarr[h, n] * matrix.matarr[n, w]
        return Matrix(mat)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.multiply_by_matrix(other).matarr
        else:
            return self.multiply_by_vector(other)

    def __add__(self, matrix):
        if not isinstance(matrix, Matrix):
            return "wrong parameters"
        if self.get_width() != matrix.get_width() or self.get_heigth() != matrix.get_heigth():
            return []
        table = [0] * self.get_heigth() * self.get_heigth()
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for w in range(self.get_width()):
            for h in range(self.get_heigth()):
                mat[h, w] += matrix.matarr[h, w]
        return Matrix(mat)

    def __sub__(self, matrix):
        if not isinstance(matrix, Matrix):
            return "wrong parameters"
        if self.get_width() != matrix.get_width() or self.get_heigth() != matrix.get_heigth():
            return []
        table = [0] * self.get_heigth() * self.get_heigth()
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for w in range(self.get_width()):
            for h in range(self.get_heigth()):
                mat[h, w] -= matrix.matarr[h, w]
        return Matrix(mat)

    def get_tril(self, k_diagonal):
        table = [0] * self.get_heigth() * self.get_width()
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for h in range(self.get_heigth()):
            for w in range(h + 1 + k_diagonal):
                mat[h, w] = self.matarr[h, w]
        return Matrix(mat)

    def get_triu(self, k_diagonal):
        table = [0] * self.get_heigth() * self.get_width()
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for h in range(self.get_heigth()):
            for w in range(h + k_diagonal, self.get_width()):
                mat[h, w] = self.matarr[h, w]
        return Matrix(mat)

    def get_diag(self, k_diagonal):
        table = [0] * self.get_heigth() * self.get_width()
        mat = np.array(table, dtype=float).reshape(self.get_heigth(), self.get_heigth())
        for h in range(self.get_heigth()):
            w = h + k_diagonal
            if 0 <= h <= self.get_heigth() and 0 <= w <= self.get_width():
                mat[h, w] = self.matarr[h, w]
        return Matrix(mat)

    @classmethod
    def forward_sub(cls, L, b):
        if not isinstance(L, Matrix) or not isinstance(b, list):
            return "wrong parameters"
        n = L.matarr.shape[0]
        x = [0] * n
        for i in range(n):
            tmp = 0
            for j in range(i):
                tmp += L.matarr[i, j] * x[j]
            x[i] = (b[i]-tmp) / L.matarr[i, i]
        return x

    @classmethod
    def back_sub(cls, U, b):
        if not isinstance(U, Matrix) or not isinstance(b, list):
            return "wrong parameters"
        n = U.matarr.shape[0]
        x = [0] * n
        for i in range(n - 1, -1, -1):
            tmp = 0
            for j in range(i + 1, n):
                tmp += U.matarr[i, j] * x[j]
            x[i] = (b[i]-tmp) / U.matarr[i, i]
        return x


