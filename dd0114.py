import sys
sys.setrecursionlimit(2500)

l, w, h = map(int,sys.stdin.readline().split())

n = int(input())

cube = [0]*20

max_size = 0
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    cube[a] = b
    max_size = a

def solution(l,w,h): 
    for i in range(max_size,-1,-1):
        if cube[i] and 2**i <= min(l,w,h):
            c = 2**i
            cnt = 1
            cube[i] -= 1
            if 1 <= h-c:
                cnt += solution(c,c,h-c)
            if 1 <= l-c:
                cnt += solution(l-c,c,h)
            if 1 <= w-c:
                cnt += solution(l,w-c,h)
            return cnt
    
    print(-1)
    exit(1)

print(solution(l,w,h))