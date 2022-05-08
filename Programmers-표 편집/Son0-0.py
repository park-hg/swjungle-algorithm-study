class Node:
    def __init__(self):
        self.flag = 0
        self.left = -1
        self.right = -1


def solution(n, k, cmd):
    linked_list = [Node() for _ in range(n)]
    for idx in range(n - 1):
        linked_list[idx].flag = 0
        linked_list[idx].left = idx - 1
        linked_list[idx].right = idx + 1

    # 마지막 노드 초기화
    linked_list[n - 1].left = n - 2
    linked_list[n - 1].flag = 0

    stack = []

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k].right
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k].left
        elif c[0] == 'C':
            linked_list[k].flag = 1

            left = linked_list[k].left
            right = linked_list[k].right
            stack.append(k)

            if left != -1:
                linked_list[left].right = right
            if right != -1:
                linked_list[right].left = left
                k = right
            else:
                k = left
        elif c[0] == 'Z':
            node_idx = stack.pop()
            linked_list[node_idx].flag = 0

            left = linked_list[node_idx].left
            right = linked_list[node_idx].right

            if left != -1:
                linked_list[left].right = node_idx
            if right != -1:
                linked_list[right].left = node_idx

    answer = ''
    for link in linked_list:
        if link.flag == 0:
            answer += 'O'
        else:
            answer += 'X'

    return answer
