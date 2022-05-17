# 19. 계란으로 계란치기(BOJ-16987)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
eggs = []
for _ in range(N):
    durability, weight = map(int, input().split())
    eggs.append((durability, weight))

if N == 1:
    print(0)
    exit(0)

max_count = 0
check = [False for _ in range(N)]

def dfs(eggs_list, cur_idx, is_egg_break):
    global max_count
    break_egg_count = is_egg_break.count(True)
    max_count = max(max_count, break_egg_count)

    if break_egg_count == N:
        print(N)
        exit(0)

    if cur_idx == N:
        return 

    if is_egg_break[cur_idx]:
        dfs(eggs_list, cur_idx + 1, is_egg_break)
        return

    cur_egg = eggs_list[cur_idx]

    for idx in range(N):
        if idx == cur_idx:
            continue
        if not is_egg_break[idx]:
            next_egg = eggs_list[idx]
            durability_egg1 = cur_egg[0] - next_egg[1]
            durability_egg2 = next_egg[0] - cur_egg[1]
            eggs_list[cur_idx] = (durability_egg1, cur_egg[1])
            eggs_list[idx] = (durability_egg2, next_egg[1])
            if durability_egg1 <= 0:
                is_egg_break[cur_idx] = True
            if durability_egg2 <= 0:
                is_egg_break[idx] = True
            dfs(eggs_list, cur_idx + 1, is_egg_break)
            eggs_list[cur_idx] = cur_egg
            eggs_list[idx] = next_egg
            if durability_egg1 <= 0:
                is_egg_break[cur_idx] = False
            if durability_egg2 <= 0:
                is_egg_break[idx] = False

dfs(eggs, 0, check)
print(max_count)