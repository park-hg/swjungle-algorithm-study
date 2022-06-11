def solution(word):
    alpha = 'AEIOU'
    llist = []

    def dfs(visited=""):
        if 5 <= len(visited):
            return

        for a in alpha:
            llist.append(visited + a)
            dfs(visited + a)

    dfs("")
    return llist.index(word) + 1
