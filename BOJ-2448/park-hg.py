import sys

N = int(sys.stdin.readline())
matrix = [[' ']*(2*N-1) for _ in range(N)]

def rec(x, y, n):
    if n == 3:
        matrix[x][y+2] = '*'
        matrix[x+1][y+1] = matrix[x+1][y+3] = '*'
        matrix[x+2][y] = matrix[x+2][y+1] = matrix[x+2][y+2] = matrix[x+2][y+3] = matrix[x+2][y+4] = '*'
        return

    rec(x, y+n//2, n//2)
    rec(x+n//2, y, n//2)
    rec(x+n//2, y+n, n//2)

rec(0, 0, N)

for r in matrix:
    print(''.join(r))
