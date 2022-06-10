import heapq

i = [1,1,2,3,5]
heapq.heapify(i)
b = [3,4]
a = heapq.heappop(i)
# i = i + b

print(i)