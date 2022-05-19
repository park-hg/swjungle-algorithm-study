import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

graph  = [[] for _ in range(N+1)] #그래프
arr = [ 0 for _ in range(N+1)] # 진출차수 
for i in range(M):
    n_list = list(map(int, input().split()))
    singer_list = n_list[1:]
    for j in range(len(singer_list) -1) :
        graph[singer_list[j]].append(singer_list[j+1])
        arr[singer_list[j+1]] += 1
    # print(graph)
    # print(arr)

def top_sort(graph, arr) :
    global answer_list
    q = deque()

    for i in range(1, len(arr)) :
        if arr[i] == 0 :
            answer_list.append(i)
            q.append(i)

    while q :

        now_idx = q.popleft()

        for node in graph[now_idx] :
            arr[node] -= 1
            if arr[node] == 0 :
                answer_list.append(node)
                q.append(node)


answer_list = []
top_sort(graph, arr)
if len(answer_list) != N :
    print("0")
else:
    for i in answer_list :
        print(i)