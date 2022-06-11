answer = 0

def solution(word):
    alpha = 'AEIOU'
    llist = []

    def dfs(visited=""):
        global answer

        if 5 <= len(visited):
            return

        for a in alpha:
            answer += 1
            llist.append(visited + a)
            dfs(visited + a)

    dfs("")
    return llist.index(word) + 1
