import sys
import heapq
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# N+1번 후보 정우는 결과기다림
# N명이 더 출마 1~ㅜ
# 사건  Q회로
# p번후보의 누적표가 x만큼 증가
# 정후표가 x장, 제가 아닌후보가 y장 더 집계된다면 당선가능성
# 최다 득표한 후보각 서로 같은수면 당선아님

N, Q = map(int, input().split())

#총 Q +1명 출마
dic = {}
for i in range(Q) :
    a, b, c = map(int, input().split())

    if a == 1 :
        if c not in dic :
            dic[c] = b
        else:
            dic[c] += b
    else:  #2번일 때
        heap = list(dic.values())
        heapq.heapify(heap)
        
        while c > 0 :
            temp = heapq.heappop(heap)
            heapq.heappush(heap, temp +1)
            c -= 1

        if b > heapq.heappop(heap) :
            print("yes")
        else:
            print("no")

