# 23. 회색 영역(BOJ-3885) 푸는 중입니다ㅠㅠ
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while(1):
    histo_n, width = map(int, input().split())
    if histo_n == 0 and width == 0:
        break
    histo_height = []
    max_height = 0
    for _ in range(histo_n):
        h = int(input())
        histo_height.append(h)
        max_height = max(max_height, h)

    max_area = width * max_height
    print('max h >> ', max_height, max_area)
    area_ink = 1 / max_area
    total_ink = 0
    color = 1
    for hh in histo_height:
        area = hh * width
        total_ink += color * area_ink * area
        print('color ', color, area)
        color -= (color / histo_n)
    total_ink += 0.01
    print(area_ink, total_ink)