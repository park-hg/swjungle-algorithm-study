import sys
import heapq
from collections import deque

input = sys.stdin.readline

# TC 수 ---
N = int(input())
# TC 수 ---


def solution():

    for i in range(N):
        # 편의점 수 ---
        conv_num = int(input())
        # 편의점 수 ---

        # 집, 편의점, 페스티벌 좌표 ---
        home_x, home_y = map(int, input().split())
        conv = []
        for _ in range(conv_num):
            conv_x, conv_y = map(int, input().split())
            conv.append([conv_x, conv_y])
        fest_x, fest_y = map(int, input().split())
        # 집, 편의점, 페스티벌 좌표 ---
        

        # bfs ---
        q = deque()
        q.append([home_x, home_y])
        for data in conv:
            if abs(data[0] - home_x) + abs(data[1] - home_y) <= 1000:
                q.append([data[0], data[1]])
                conv.remove(data)

        flag = 0
        while q:
            nx, ny = q.popleft()
            if abs(fest_x - nx) + abs(fest_y - ny) <= 1000:
                print("happy")
                flag = 1
                break

            for data in conv:
                if abs(data[0] - nx) + abs(data[1] - ny) <= 1000:
                    q.append([data[0], data[1]])
                    conv.remove(data)

        if flag == 0:
            print("sad")
        # bfs ---

    return 0


solution()
