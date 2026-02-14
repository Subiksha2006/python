A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

r1 = len(A)
c1 = len(A[0])
r2 = len(B)
c2 = len(B[0])

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    C = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    for row in C:
        print(row)
