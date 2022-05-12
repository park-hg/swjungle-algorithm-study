from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)
    d = defaultdict(set)
    counter = defaultdict(int)
    for r in report:
        user, reported = r.split()
        d[user].add(reported)
        counter[reported] += 1

    answer = []
    for id in id_list:
        cnt = 0
        for r in d[id]:
            if counter[r] >= k:
                cnt += 1
        answer.append(cnt)

    return answer