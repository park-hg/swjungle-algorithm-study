import sys

d, first = sys.stdin.readline().split()

d = int(d)
wlist = []

wlist = [[]for _ in range(81)]

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

    for i in wlist[len(a)+1]:
        
        ind=lena
        for j in range(lena) :
            if i[j] != a[j]:
                ind = j
            
            if i[ind+1:] in a :
                last = 1 
                q.append(i)
            break


    if last == 0 and maxn < lena:
        maxn = lena
        maxw = a

print(wlist)
print(maxw)