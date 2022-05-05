import sys
input = sys.stdin.readline

S, C = map(int, input().split())
onions = [0] * (S)
max_onion = 0
onion_sum = 0
for i in range(S):
    onions[i] = int(input())
    onion_sum += onions[i]
    if onions[i] > max_onion:
        max_onion = onions[i]

start = 0
end = max_onion
ans = 0
while(start <= end) :
    mid = (start+end) // 2
    cnt = 0
    if(mid==0) :
        break
    for onion in onions:
        cnt_to_add = onion // mid
        cnt += cnt_to_add
    if cnt < C:
        end = mid-1
    else:
        start = mid+1
    
print(onion_sum-(end*C))
    
    
