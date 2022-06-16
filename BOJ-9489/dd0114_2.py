import sys

while True:
    n, k = map(int,sys.stdin.readline().split())

    if n == 0 and k == 0:
        break
    answer = 0
    t_list = list(map(int,sys.stdin.readline().split()))
    links = [[] for _ in range(n+1)]
    find_parent = [0]*(n+1)
    cnt = 0
    ind = 1
    check = 1
    if n == 1 :
        print(0)
        continue

    while check:
        buf = []
        links[cnt].append(ind)
        find_parent[ind] = cnt
        
        if ind == n-1:
            break

        if t_list[ind]+1 != t_list[ind+1]:
            cnt += 1 
        ind += 1    

    parent = find_parent[t_list.index(k)]

    if parent == 0:
        print(0)
    else :
        grand_p = find_parent[parent]

        for i in links[grand_p]:
            if i != parent:
                answer += len(links[i])
        print(answer)