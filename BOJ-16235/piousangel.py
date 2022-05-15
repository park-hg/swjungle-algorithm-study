#죄송합니다. 다시 공부해서 풀겠습니다.

import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())  

#봄 나무들이 자신의 나이만큼 양분을 먹고 나이가 1 증가(어린아이부터 양분을 먹고 해당 양분 못먹으면 즉시 사망)
#여름 죽은 나무들이 양분이 되는데 그 양분은 그 나무의 나이//2
#가을 번식하는 나무의 조건 5의 배수 인접한 8칸에 나이가 1인 나무가 생김 땅을 벗어나는 칸에는 나무가 안생김
#겨울 땅을 돌아다니면서 땅에 양ㅇ분추가 각칸에 추가되는 양분의 양은 A[r][c]

board = []
r = 0
c = 0
for i in range(N):
    board.append(list(map(int, input().split())))  #추가되는 양분 수


yangbun_list = [ [5] * N for i in range(N)]
# tree_list = [[[]*N for _ in range(N)] for _ in range(N)]
tree_dic = {}

for i in range(N):
    for j in range(N):
        if str(i)+str(j) not in tree_dic :
            tree_dic[str(i)+str(j)] = []

for i in range(M):
    x, y, z = map(int, input().split())
    r = x - 1
    c = y - 1
    tree_dic[str(r)+str(c)].append(z)

def spring() :
    for i in range(N) :
        for j in range(N) :
            total_yangbun = yangbun_list[i][j]
            plus_yangbun = 0
            #여기 리스트 있다
            temp = sorted(tree_dic[str(i)+str(j)])
            temp_list = []
            # print(temp)
            for k in range(len(temp)):
            
                if total_yangbun >= temp[k] :
                    print("temp[k]", temp[k])
                    total_yangbun -= temp[k]
                    temp_list.append(temp[k]+1)
                else:
                    plus_yangbun += temp[k] //2
                    
            yangbun_list[i][j] += plus_yangbun
            tree_dic[str(i)+str(j)] = temp_list
            
        
def fall() :

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(N) :
        for j in range(N) :
            temp = tree_dic[str(i)+str(j)]
            for tree in temp :
                # print("tree!!!!!!!", tree)
                if tree % 5 == 0 :
                    for k in range(8):
                        nx = j + dx[k]
                        ny = i + dy[k]
                    if 0 <= nx < N and 0 <= ny < N :
                        tree_dic[str(nx)+str(ny)].append(1)

def winter() :
    for i in range(N):
        for j in range(N):
            yangbun_list[i][j] += board[i][j]


print(tree_dic)

while K > 0 :
    spring()
    fall()
    winter()
    K -=1

answer = 0

print("====")
print(tree_dic)
# print(yangbun_list)

for i in range(N) :
    for j in range(N):
        for tree in tree_dic[str(i)+str(j)] :
            answer += len(tree)

print(answer)