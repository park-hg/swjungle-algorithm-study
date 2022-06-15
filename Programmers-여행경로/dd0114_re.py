from collections import deque
import copy

global root
root = []

def fly(ans,check,now,cnt,finish):
    global root
    if root != []:
        return
    cnt += 1
    
    while check[now]:
        new_check = copy.deepcopy(check)
        next_air = new_check[now].popleft()
        
        new_ans = copy.deepcopy(ans)
        new_ans.append(next_air)
        
        if cnt == finish:
            root = ans
            return

        elif new_check[next_air] != deque([]):
            fly(new_ans, new_check, next_air, cnt,finish)

def solution(tickets):
    airport = set([])
    finish = len(tickets)
    for i in tickets:
        start, end = i
        airport.add(start)
        airport.add(end)
    
    air_num = len(airport)
    # check = 0
    links = [[] for _ in range(air_num)]
    airport = list(airport)
    airport.sort()
    # num_tickets =[]
    for i in tickets:
        start, end = i
        e_idx = airport.index(end)
        s_idx = airport.index(start)
        # check[e_idx] +=1
        links[s_idx].append(e_idx)
        # num_tickets.append((s_idx,e_idx))

    for i in range(air_num):
        links[i].sort()
        links[i] = deque(links[i])
        
    fly([airport.index("ICN")],links,airport.index("ICN"),0,finish)
        
    answer = []
    for i in root:
        answer.append(airport[i])
    
    return answer

# tic = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

tic = [["ICN", "A"], ["ICN","B"],["B","ICN"]]
print(solution(tic))