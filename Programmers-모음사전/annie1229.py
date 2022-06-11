def solution(word):
    order = 0
    add = [780, 155, 30, 5, 0]
    for idx, w in enumerate(word):
      # print('add',add[idx], idx)
      if w == 'A':
        order += 1
      elif w == 'E':
        order += add[idx] * 1 + 2
      elif w == 'I':
        order += add[idx] * 2 + 3
      elif w == 'O':
        order += add[idx] * 3 + 4
      elif w == 'U':
        order += add[idx] * 4 + 5
    print('answer ',order)
    return order

solution("AAAAA") #5
solution("AAAAE") #6
solution("AAAE") #10  = 1 + 1 + 1 + 5 + 1
solution("I") #1563  = 780 + 780 + 3
solution("EIO") #1189 = 780 + 155 + 155 + 30 + 30 + 30 + 5 + 4

# I면 A로 시작하는 단어 1 * 5 * 5 * 5* 5 =625 + 125 + 25 + 5 = 780
# E로 시작하는 단어 1 * 5 * 5 * 5 * 5 = 625 1250 780 *2 = 1560
# I로 시작하고   + A, E, I = 3