# 효율성 해결 못해서 프로그래머스 질문 게시판 참고했습니다

def solution(info, query):
  
    _map = {}
    answer = []
    llist = []
    score = []

    for data in info:
        temp = list(map(str, data.split()))
        for h in [temp[0], '-']:
            for i in [temp[1], '-']:
                for j in [temp[2], '-']:
                    for k in [temp[3], '-']:
                        t = h + i + j + k
                        if t in _map:
                            _map[t].append(int(temp[4]))
                        else:
                            _map[t] = [int(temp[4])]
                            
    for val in _map.values():
        val.sort()

    for qry in query:
        cnt = 0
        temp = [q for q in list(map(str, qry.split())) if q != 'and']
        temp_c = ''.join(temp[:4])
        if temp_c not in _map:
            answer.append(0)
            continue
        score_list = _map[temp_c]
        size = len(score_list)
        left, right = 0, size - 1

        while left <= right:
            mid = (left + right) // 2
            target = score_list[mid]

            if target < int(temp[4]):
                left = mid + 1
            else:
                right = mid - 1

        answer.append(size - left)

    return answer
  
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
#          ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# _map = {
#     "cpp": 0, "java": 1, "python": 2,
#     "backend": 0, "frontend": 1,
#     "junior": 0, "senior": 1,
#     "chicken": 0, "pizza": 1
# }


# def solution(info, query):
#     answer = []
#     llist = []
#     score = []

#     for data in info:
#         temp = list(map(str, data.split()))
#         llist.append(''.join([str(_map[d])
#                      for d in temp if not d.isdigit()][:4]))
#         score.append(int(temp[4]))

#     for qry in query:
#         cnt = 0
#         temp = list(map(str, qry.split()))

#         qry = ''
#         for q in temp[:-1]:
#             if q == '-':
#                 qry += '-'
#             elif q != 'and' and not q.isdigit():
#                 qry += str(_map[q])

#         for idx, p in enumerate(llist):
#             if qry == p:
#                 if int(temp[-1]) <= score[idx]:
#                     cnt += 1
#                     continue
#             elif '-' in qry:
#                 flag = 1
#                 for i in range(4):
#                     if qry[i] != '-':
#                         if qry[i] != p[i]:
#                             flag = 0
#                             break
#                 if flag == 1 and int(temp[-1]) <= score[idx]:
#                     cnt += 1
#                     continue

#         answer.append(cnt)

#     return answer


# info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
#         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

# print(solution(info, query))
