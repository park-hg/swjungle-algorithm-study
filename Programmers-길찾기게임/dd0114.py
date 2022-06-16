import sys
sys.setrecursionlimit(2500)

pre_list = []
post_list = []

def pre(n_i):
    if n_i == []:
        return
    x_node = max(n_i)
    x_index = n_i.index(x_node)

    pre_list.append(x_node[2])
    pre(n_i[:x_index])
    pre(n_i[x_index+1:])

def post(n_i):
    if n_i == []:
        return
    
    x_node = max(n_i)
    x_index = n_i.index(x_node)

    post(n_i[:x_index])
    post(n_i[x_index+1:])
    post_list.append(x_node[2])

def solution(nodeinfo):
    answer = []
    new_node = []

    for i in range(len(nodeinfo)):
        new_node.append((nodeinfo[i][1], nodeinfo[i][0],i+1))

    new_node.sort(key=lambda x :x[1])

    pre(new_node)
    post(new_node)

    answer.append(pre_list)
    answer.append(post_list)

    return answer

ni = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

print(solution(ni))
