import sys

t = int(input())

for _ in range(t):
    num, link = map(int,sys.stdin.readline().split())
    
    visit = [False] *(num+1)
    visit[0] = True
    links = [[] for _ in range(num+1)]
    b_w = [0]*(num+1)
    break_point = 0

    for i in range(link):
        a, b = map(int,sys.stdin.readline().split())
        links[a].append(b)
        links[b].append(a)
    
    for i in range(1,num+1):
        if visit[i] == 0 and not break_point:
            visit[i] = 1
            q = [i]
            while q :
                pop = q.pop()
                for j in links[pop]:
                    if visit[pop] == 1:
                        if visit[j] == 0:
                            visit[j] = 2
                            q.append(j)
                        elif visit[j] ==2:
                            continue
                        else :
                            q =False
                            break_point = 1            
                            break

                    else :
                        if visit[j] == 0:
                            visit[j] = 1
                            q.append(j)
                        elif visit[j] ==1:
                            continue
                        else :
                            q =False
                            break_point = 1            
                            break
    
    if break_point == 1 :
        print("NO")
    else :
        print("YES")

