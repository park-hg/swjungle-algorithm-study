import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = input()

# print(total_length)
# 1~N까지 저장해놓았다
# 13개면 11까지다 
# 10부터 간다
# 15개면 12
# 17개면 13
# 19개면 14
# 21개면 15

length = len(n)
temp = length - 9
total_length = 9 + (temp//2)

number_box = []
for i in range(1, total_length+1) :
    number_box.append(i)

def dfs(target, visited, idx, answer) :

    if idx == len(target) :
        print(*answer)
        sys.exit()

    str1 = ""
    for i in range(idx, idx+2):
        if i >= len(target) :
            continue
            
        str1 = str1 + target[i]
        inum = int(str1)
        if inum > len(visited) :
            continue
        
        if visited[inum] :
            continue

        visited[inum] = True
        answer.append(inum)
        dfs(target, visited, i+1, answer)
        visited[inum] = False
        answer.pop()
        
answer = []
visited = [False] * (total_length + 1)

dfs(n, visited, 0, answer)
