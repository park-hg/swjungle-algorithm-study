import sys

n,s = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0
ans = 100000000

def find(start,end):
    result = 0
    for i in range(start,end+1):
        result += num_list[i]
    return result

while right < n and ans != 1 :
    
    a = find(left, right)
    if left == right :
        a = num_list[right]
        if a >= s :
            ans = 1 
            break
        else :
            right +=1
    else :
        if a >= s:
            ans = min(ans,right-left+1)
            left +=1 
        else :
            right +=1

print(ans)