import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
S, W = [], []
for _ in range(N):
    s, w = map(int, sys.stdin.readline().split())
    S += s,
    W += w,

answer = 0
def backtrack(start):
    global answer
    
    if start == N:
        answer = max(answer, sum([s<=0 for s in S]))
        return

    if S[start] > 0:
        for i in range(N):
            if i != start and S[i]:
                S[start] -= W[i]
                S[i] -= W[start]
                backtrack(start+1)
                S[start] += W[i]
                S[i] += W[start]
    else:
        backtrack(start+1)

backtrack(0)
print(answer)
