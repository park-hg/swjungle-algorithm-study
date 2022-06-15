import sys
from collections import deque
sys.stdin = open('sample.txt')
open = sys.stdin.readline

while True :
    a, b = map(int, input().split())  # a는 노드 수, b는 사촌을 구해야하는 노드
    if a == 0 and b == 0 :
        break
    else:
        n_list = list(map(int, input().split()))

    max_num = max(n_list)
    graph = [[] for _ in range(max_num+1)] #32까지 그래프를 만들어 놨다
    idx = 0 
    temp = 0
    flag = False
    k = 0
    for n in n_list :
        if k == 0 :
            k += 1
            continue
        if flag == False :   #달라서 바뀐 지점
            temp = n
            graph[n_list[idx]].append(temp)
            flag = True
        else:
            if n == temp + 1 : #연속되었으면
                graph[n_list[idx]].append(n)
                temp = n
            else :     #연속되지 않았으면 다음 idx의 자식으로 추가
                idx += 1
                graph[n_list[idx]].append(n)
                temp = n

    q = deque()
    q.append([n_list[0], 0])
    dic = {}
    
    while q :

        now, cnt  = q.popleft()
        
        dic[now] = cnt
        if b in graph[now] :
            q.append([b, cnt+1])
            continue
        
        for node in graph[now] :
            q.append([node, cnt+1])
    
    answer = 0
    
    for value in dic.values():
        if value == dic[b] :
            answer += 1

    print(answer-1)