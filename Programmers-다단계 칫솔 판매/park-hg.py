from collections import defaultdict
def solution(enroll, referral, seller, amount):
    graph = defaultdict(list)
    for a, b in zip(enroll, referral):
        graph[a].append(b)
    d = defaultdict(int)

    for name, amount in zip(seller, amount):
        cur_amount = amount * 100
        d[name] += cur_amount
        while graph[name]:
            if cur_amount == 0:
                break
            next_amount = cur_amount//10
            d[name] -= next_amount
            d[graph[name][0]] += next_amount
            name = graph[name][0]
            cur_amount = next_amount
    ans = [d[name] for name in enroll]
    return ans