import iksan003

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]


def tampil_matrix(matrix):
    for baris in matrix:
        print(baris)


print("Matriks A:")
tampil_matrix(A)

print("\nMatriks B:")
tampil_matrix(B)


print("\nHasil Penjumlahan:")
tampil_matrix(iksan003.penjumlahan(A, B))


print("\nHasil Pengurangan:")
tampil_matrix(iksan003.pengurangan(A, B))


print("\nHasil Perkalian:")
tampil_matrix(iksan003.perkalian(A, B))


print("\nHasil Transpose A:")
tampil_matrix(iksan003.transpose(A))