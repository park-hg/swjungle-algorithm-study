from collections import deque

def solution(N, stages):
    answer = []

    ratio = [0]*N
    n_list = []

    for i in range(len(stages)):
        if stages[i] == N+1:
            continue
        else:
            ratio[stages[i]-1] += 1

    total_n = len(stages)
    for i in range(len(ratio)):
        if(ratio[i] != 0):
            temp = ratio[i]
            ratio[i] = temp / total_n
            total_n -= temp

    q = deque()

    for i in range(len(ratio)):
        q.append([i+1, ratio[i]])

    while q :

        now_prior, now_name = q.popleft()
        chk = False

        for options in q:
            # print("prior",options[0])
            # print("name",options[0])
            if now_name < options[1] :
                 chk = True
            else:
                if now_name == options[1] :
                    if now_prior > options[0] :
                        chk = True
        if chk :
            q.append([now_prior, now_name])
        else:
            n_list.append(now_prior)

    return n_list