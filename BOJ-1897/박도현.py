import sys

d, first = sys.stdin.readline().split()

d = int(d)
wlist = []

wlist = [[]for _ in range(82)]

for _ in range(d):
    a = input()
    wlist[len(a)].append(a)

q = [first]
lastlist =[]
maxw = first
maxn = len(first)

while q :
    a= q.pop()
    last = 0
    lena = len(a)

    for i in wlist[lena+1]:
        
        if len(set(i) - set(a)) >= 2:
            continue
        
        ind=lena
        for j in range(lena) :
            if i[j] != a[j]:
                ind = j            
                break

        if i[ind+1:] == a[ind:] :
            if i not in q:
                q.append(i)
            last = 1 

    if last == 0 and maxn < lena:
            maxn = lena
            maxw = a

if maxw == first and first not in  wlist[len(first)]:
    print(0)
else:
    print(maxw)