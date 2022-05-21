# 23. 회색 영역(BOJ-3885)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while(1):
    histo_n, width = map(int, input().split())
    if histo_n == 0 and width == 0:
        break

    histo_height = [0 for _ in range(11)]
    max_data = 0
    for _ in range(histo_n):
        data = int(input())
        histo_height[data//width] += 1
        max_data = max(max_data, data)
        
    max_idx = max_data // width
    max_height = max(histo_height)
    max_area = width * max_height
    area_ink = 1 / max_area
    total_ink = 0

    for idx, hh in enumerate(histo_height):
        area = hh * width
        total_ink += ((max_idx - idx) / max_idx) * area_ink * area
    total_ink += 0.01
    print(total_ink)