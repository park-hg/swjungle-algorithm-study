import sys

while True:
    n,w = map(int,sys.stdin.readline().split())

    if n == 0 and w == 0 :
        break

    else :
        ink = 0
        hist_list = [0]*11
        maxlen = 0
        maxhist = 0
        maxhist_num = 0
        for j in range(n):
            new = int(sys.stdin.readline().rstrip())
            a = (new)//w
            hist_list[a] +=1
            maxlen = max(maxlen,a)
            
            if hist_list[a] > maxhist:
                maxhist_num = a
                maxhist = hist_list[a]
        
        ans = 0.01
        for j in range(maxlen):
            ans += ((maxlen-j)/maxlen) * (hist_list[j]/maxhist)

        print(ans)
