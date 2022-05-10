#형규형님께서 친절하게 설명해주셨습니다.
import sys
import math
sys.stdin = open('sample.txt')
input = sys.stdin.readline


x, y, c = map(float, input().split())

x = x*1000
y = y*1000
c = c*1000

left_value = 0
right_value = min(x, y)  #증가함수 이므로
mid_value = 0
answer = 0

def find_a(a) :
     return c/(math.sqrt(x**2 - a**2)) + c/(math.sqrt(y**2 - a**2))

while left_value < right_value :
    mid_value = (right_value + left_value) // 2

    if(find_a(mid_value)) < 1 :
        left_value = mid_value + 1
        # answer += mid_value
    else:
        right_value = mid_value -1
    
print("{0:.3f}".format(left_value/1000))