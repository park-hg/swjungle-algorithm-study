def solution(word):
    l = ['A', 'E', 'I', 'O', 'U']
    total = []
    answer = 0
    def dfs(w, cnt):
        if len(w) > 5:
            return

        if w != '':
            total.append(w)
        for char in l:
            dfs(w+char, cnt+1)
    dfs('', 0)

    return total.index(word)+1