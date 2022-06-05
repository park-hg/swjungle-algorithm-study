def solution(board, skill):
    answer = 0
    row = len(board)
    col = len(board[0])
    box = [[0]* (col+1) for _ in range(row+1)]
    
    #type, r1, c1, r2, c2, degree
    for info in skill :
        if info[0] == 1 : #내구도 낮춤
            box[info[1]][info[2]] -= info[5]
            box[info[1]][info[4]+1] += info[5]
            box[info[3]+1][info[2]] += info[5]
            box[info[3]+1][info[4]+1] -= info[5]
        else:
            box[info[1]][info[2]] += info[5]
            box[info[1]][info[4]+1] -= info[5]
            box[info[3]+1][info[2]] -= info[5]
            box[info[3]+1][info[4]+1] += info[5]
    
    #행 누적
    for i in range(row):
        for j in range(col):
            box[i][j + 1] += box[i][j]
 
    # 열 누적
    for j in range(col):
        for i in range(row):
            box[i + 1][j] += box[i][j]
 
    for i in range(row):
        for j in range(col):
            board[i][j] += box[i][j]
            
            if board[i][j] > 0 : 
                answer += 1
                
    return answer