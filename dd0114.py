def solution(board, skill):
    count = len(board) * len(board[0])
    
    for i in skill:
        t = i[0]
        r1 = i[1]
        c1 = i[2]
        r2 = i[3]
        c2 = i[4]
        degree = i[5]

        if t == 1:
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    board[r][c] -= degree
                    if board[r][c] == 0:
                        count -= 1
        else :
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    board[r][c] += degree
                    if board[r][c] == 0:
                        count += 1
    answer = count
    
    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board, skill))