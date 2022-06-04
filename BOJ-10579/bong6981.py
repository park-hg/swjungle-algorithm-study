ans = ''

def find(s, sidx, arr, num_set):
    print("---")
    print(s, sidx, arr, num_set)
    global ans
    if sidx == len(s):
       ans = " ".join([str(i) for i in arr])
       print(ans)
       return True
    
    ## 1
    print(s[sidx])
    if int(s[sidx]) in num_set:
        arr.append(int(s[sidx]))
        num_set.remove(int(s[sidx]))
        if find(s, sidx+1, arr, num_set):
            return True
        num_set.add(int(s[sidx]))
        arr.pop()
    
    if sidx+1 < len(s):
        print("hi!!")
        print(s, sidx, arr, num_set)
        print(s[sidx:sidx+2])

        if int(s[sidx:sidx+2]) in num_set:
            arr.append(int(s[sidx:sidx+2]))
            num_set.remove(int(s[sidx:sidx+2]))
            if find(s, sidx+2, arr, num_set):
                return True
            num_set.add(int(s[sidx:sidx+2]))
            arr.pop()
    return False
    

s = input()
cnt = len(s)

start = 1
end = 50

num = 0
while(start <= end):
    mid = (start + end) // 2
    c = 0
    if mid < 10:
        c = mid
    else:
        c = 9
        c += (mid - 9) * 2

    if c == cnt:
        num = mid
        break 

    if c < cnt:
        start = mid + 1
    else:
        end = mid - 1

find(s, 0, [], set(i for i in range(1, num+1)))
print(ans)

   



