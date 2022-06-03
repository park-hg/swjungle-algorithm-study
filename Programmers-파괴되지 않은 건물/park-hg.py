def solution(board, skill):
    N, M = len(board), len(board[0])
    imos = [[0]*(M+1) for _ in range(N+1)]
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk
        if type == 1:
            degree *= -1
            
        imos[r1][c1] += degree
        imos[r1][c2+1] -= degree
        imos[r2+1][c1] -= degree
        imos[r2+1][c2+1] += degree
    
    for i in range(N):
        for j in range(1, M):
            imos[i][j] += imos[i][j-1]
            
    for i in range(1, N):
        for j in range(M):
            imos[i][j] += imos[i-1][j]
            
    for i in range(N):
        for j in range(M):
            board[i][j] += imos[i][j]
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1
        
    return answer