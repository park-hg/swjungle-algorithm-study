# 19. 계란으로 계란치기(BOJ-16987) 아직 푸는 중입니다..ㅠ
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

def dfs(eggs_list, cur_idx, is_egg_break, break_egg_count):
    # print(eggs_list[cur_idx], 'dfs ', eggs_list, is_egg_break, break_egg_count)
    global max_count
    max_count = max(max_count, break_egg_count)
    if is_egg_break.count(True) == N:
        print(N)
        exit(0)

    if cur_idx == N:
        # print('마지막 계란입니다. ', eggs_list, is_egg_break, break_egg_count - 1)
        max_count = max(max_count, break_egg_count)
        return 

    if is_egg_break[cur_idx]:
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
                break_egg_count += 1
                is_egg_break[cur_idx] = True
            if durability_egg2 <= 0:
                break_egg_count += 1
                is_egg_break[idx] = True
            dfs(eggs_list, cur_idx + 1, is_egg_break, break_egg_count)
            eggs_list[cur_idx] = cur_egg
            eggs_list[idx] = next_egg
            if durability_egg1 <= 0:
                break_egg_count -= 1
                is_egg_break[cur_idx] = False
            if durability_egg2 <= 0:
                break_egg_count -= 1
                is_egg_break[idx] = False

dfs(eggs, 0, check, 0)
print(max_count)