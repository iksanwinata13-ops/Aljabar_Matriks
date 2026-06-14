def penjumlahan(A, B):
    hasil = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            hasil[i][j] = A[i][j] + B[i][j]

    return hasil


def pengurangan(A, B):
    hasil = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            hasil[i][j] = A[i][j] - B[i][j]

    return hasil


def perkalian(A, B):
    hasil = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                hasil[i][j] += A[i][k] * B[k][j]

    return hasil


def transpose(A):
    hasil = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            hasil[j][i] = A[i][j]

    return hasil