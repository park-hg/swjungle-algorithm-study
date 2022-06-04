def solution(board, skill):
    n = len(board) 
    m = len(board[0])
    box = [([0]*m) for _ in range(n)]
    answer = n*m

    for i in skill:
        t = i[0]
        r1 = i[1]
        c1 = i[2]
        r2 = i[3]
        c2 = i[4]
        degree = i[5]

        if t == 1:
            degree = -1*degree

        box[r1][c1] += degree
        if r2+1 < n:
            box[r2+1][c1] -= degree
        if c2+1 < m:
            box[r1][c2+1] -= degree
        if r2+1 < n and c2+1 < m:
            box[r2+1][c2+1] += degree

    for i in range(n):
        for j in range(1,m):
            box[i][j] += box[i][j-1]
    
    for i in range(m):
        for j in range(1,n):
            box[j][i] += box[j-1][i]
    
    for i in range(n):
        for j in range(m):
            if box[i][j]+board[i][j] <= 0:
                answer -= 1

    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board, skill))