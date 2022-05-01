#못풀어서 답을 보았습니다.

import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

stars_list = [[' ']*2*n for _ in range(n)]  #2*n로 커버가능

def dfs(i, j, size):
    if size == 3:
        stars_list[i][j] = '*'
        stars_list[i + 1][j - 1] = "*"
        stars_list[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars_list[i + 2][j - k] = "*"
    
    else:
        half = size//2          # 3*2^k
        dfs(i, j, half)
        dfs(i + half, j - half, half)
        dfs(i + half, j + half, half)

dfs(0, n - 1, n)
for star in stars_list:
    print("".join(star))

