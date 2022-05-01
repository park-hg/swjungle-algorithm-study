# 3. 별 찍기 - 11(#2448)
import sys

N = int(sys.stdin.readline())
paper = [[' ' for _ in range(2*N)] for _ in range(N)]

def draw_star(i, cnt):
    if i >= N:
        return
    if cnt <= 0 or cnt > 2*N:
        return
        
    if paper[i][cnt] != '*':
        paper[i][cnt] = '*'
        paper[i+1][cnt-1] = '*'
        paper[i+1][cnt+1] = '*'
        for jj in range(cnt-2, cnt+3):
            paper[i+2][jj] = '*'
    else:
        paper[i][cnt] = ' '
        paper[i+1][cnt-1] = ' '
        paper[i+1][cnt+1] = ' '
        for jj in range(cnt-2, cnt+3):
            paper[i+2][jj] = ' '
    if i < N - 1:
        draw_star(i+3, cnt-3)
        draw_star(i+3, cnt+3)

draw_star(0, N-1)
for p in paper:
    print(*p, sep='')