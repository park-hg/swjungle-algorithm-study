# 7. 파닭파닭(BOJ #14627) 아직 푸는 중
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S, C = map(int, input().split())
ingredients = []
total = 0
for _ in range(S):
    ingredient = int(input())
    ingredients.append(ingredient)
    total += ingredient
start = 0
end = max(ingredients)
result = 0

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        start = 1
        continue
    chicken_total = 0
    
    for i in ingredients:
        chicken_total += i // mid
        
    if chicken_total >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(total - (result * C))