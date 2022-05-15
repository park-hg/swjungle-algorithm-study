def solution(id_list, report, k):
  user = {}
  cnt = {}
  for id in id_list:
    user[id] = []
    cnt[id] = 0
  
  for r in set(report):
    a, b = r.split()
    user[a].append(b)
    cnt[b] += 1

  banned = []
  for id in cnt:
    if cnt[id] >= k:
      banned.append(id)

  answer = [0] * len(id_list)
  for i, u in enumerate(user):
    for b in banned:
      if b in user[u]:
        answer[i] += 1
      
  # print(answer)
  return answer
