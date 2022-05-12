def solution(id_list, report, k):
    count = dict()
    llist = dict()
    for name in id_list:
        count[name] = 0
        llist[name] = []

    report.sort()
    for rpt in report:
        p1, p2 = map(str, rpt.split())
        if p2 not in llist[p1]:
            llist[p1].append(p2)
            count[p2] += 1

    answer = []
    for r in llist:
        cnt = 0
        for a in llist[r]:
            if k <= count[a]:
                cnt += 1
        answer.append(cnt)

    return answer
