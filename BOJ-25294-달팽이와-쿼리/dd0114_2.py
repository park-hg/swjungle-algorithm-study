import sys

nn = int(input())

for _ in range(nn):

    a = sys.stdin.readline().strip()
    # a  = list(map(int,sys.stdin.readline().split()))
    
    if a[0] == "1":
        trash, n, x, y = map(int,a.split())
        # trash, n, x, y = a
        if x == n//2+1 and y == n//2 +1:
            print(n**2)
            continue

        up = x-1
        down = n -x
        left = y-1
        right = n - y
        
        tmp = min(up,down,left,right)
        side = (n-2*tmp)-1

        base = n**2 - (n-2*tmp)**2
        
        ans_x = x-tmp
        ans_y = y-tmp


        if tmp == up and ans_y <= side:
            ans = ans_y    

        elif tmp == right and ans_x <= side:
            ans = side+ans_x

        elif tmp == down and ans_y > 1:
            ans = 3*side - (ans_y-2)

        else: 
            ans = 4*side - (ans_x-2)

        print(ans+base)

    else :

        trash, n, z = map(int,a.split())
        
        if z == n**2:
            print(n//2+1, end=' ')
            print(n//2+1)
            continue

        base = 0
        side = n-1
        for i in range(n//2+1):
            if base < z <= base + 4*side:
                break
            else :
                base += 4*side
                side -=2
                
        layer = i
        start = z-base

        for i in range(1,5):
            if start <= side*i:
                break
        
        if i == 1:
            new_y = layer + start
            new_x = layer +1

        elif i == 2:
            new_y = layer+side+1
            new_x = layer+start-side

        elif i == 3:
            new_y = layer + 3*side+2-start
            new_x = layer + side +1

        else:
            new_y = layer + 1
            new_x = layer + 4*side+2-start

        print(new_x,end=' ')
        print(new_y)