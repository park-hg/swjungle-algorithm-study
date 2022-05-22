import sys
sys.stdin = open('input.txt')

A, B, N = map(int, sys.stdin.readline().split())

l = []
blue_end, red_end = 0, 0

for _ in range(N):
    t, c, m = sys.stdin.readline().split()
    t, m = int(t), int(m)
    if c == 'B':
        cur_time = max(blue_end, t)
        for _ in range(m):
            l.append((cur_time, c))
            cur_time += A
        blue_end = cur_time
    elif c == 'R':
        cur_time = max(red_end, t)
        for _ in range(m):
            l.append((cur_time, c))
            cur_time += B
        red_end = cur_time

l.sort()

blue, red = [], []
for i, (t, c) in enumerate(l):
    if c == 'B':
        blue.append(str(i+1))
    else:
        red.append(str(i+1))

print(len(blue))
print(' '.join(blue))
print(len(red))
print(' '.join(red))

        
