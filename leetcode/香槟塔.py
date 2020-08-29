poured=6
query_row=2
query_glass=0
A = [[0] * k for k in range(1, 102)]
A[0][0] = poured
for r in range(query_row + 1):
    for c in range(r + 1):
        q = (A[r][c] - 1.0) / 2.0
        if q > 0:
            # A[r][c]的流入A[r+1][c]和A[r+1][c+1]
            A[r + 1][c] += q
            A[r + 1][c + 1] += q
print(min(1, A[query_row][query_glass]))