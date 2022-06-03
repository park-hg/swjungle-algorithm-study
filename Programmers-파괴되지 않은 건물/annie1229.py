def solution(board, skill): #시간초과
  answer = 0
  for sk in skill:
    ty, r1, c1, r2, c2, degree = sk
    if ty == 1:
      for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
          board[r][c] -= degree
    elif ty == 2:
      for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
          board[r][c] += degree
  # print('board', board)
  for b in board:
    for bb in b:
      if 0 < bb:
        answer += 1
  # print('answer', answer)
  return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])