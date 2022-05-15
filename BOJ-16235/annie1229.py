# 17. 나무재테크(BOJ-16235) 시간초과..
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
trees = []
nutrient = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x, y, age = map(int, input().split())
    trees.append([x - 1, y - 1, age])

def spring():
    trees.sort(key=lambda x:x[2])
    die_trees = []
    breed_trees = []

    for idx, tree in enumerate(trees):
        x, y, age = tree
        if nutrient[x][y] >= age:
            nutrient[x][y] -= age
            age += 1
            if age % 5 == 0:
                breed_trees.append(tree)
            trees[idx] = [x, y, age]
        else:
            die_trees.append(tree)

    return die_trees, breed_trees

def summer(die_trees):
    for tree in die_trees:
        x, y, age = tree
        trees.remove(tree)
        nutrient[x][y] += (age // 2)
    
def autumn(breed_trees):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for tree in breed_trees:
        x, y, age = tree
        for n in range(8):
            new_tree_x = x + dx[n]
            new_tree_y = y + dy[n]
            if new_tree_x >= 0 and new_tree_x < N and new_tree_y >= 0 and new_tree_y < N:
                trees.append([new_tree_x, new_tree_y, 1])

def winter():
    global nutrient
    nutrient = [[c + d for c, d in zip(a, b)] for a, b in zip(nutrient, A)]

for year in range(K):
    dies, breeds = spring()
    summer(dies)
    autumn(breeds)
    winter()
    
print(len(trees))


