import sys

case = int(input())
pos = 1000**2

for _ in range(case):
    store_num = int(input())

    stores = []

    a,b = map(int,sys.stdin.readline().split())
    home = (a,b)
    for _ in range(store_num):
        a, b = map(int,sys.stdin.readline().split())
        stores.append((a,b))
    a,b = map(int,sys.stdin.readline().split())
    end = (a,b)
    stores.sort()
    stores.append(end)
    visited = (store_num+1) * [False]

    q = [home]

    while q :
        now_x,now_y = q.pop()

        for i in range(store_num):
            if visited[i] :
                continue

            else:
                store_x = stores[i][0] 
                store_y = stores[i][1]
                
                if (now_x - store_x)**2 > pos:
                    break

                elif (now_x - store_x)**2 + (now_y - store_y)**2 <= pos:
                    visited[i] = True
                    q.append(stores[i])

    if visited[-1] == True:
        print("happy")
    else:
        print("sad")
