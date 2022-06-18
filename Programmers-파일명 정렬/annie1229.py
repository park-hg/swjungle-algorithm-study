from heapq import heappush, heappop

def solution(files):
    answer = []
    sort_q = []
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for idx, file in enumerate(files):
        num_temp = ''
        file_num = 0
        head = ''
        for text in file:
            if text in nums:
                num_temp += text
                if 5 == len(num_temp):
                    file_num = int(num_temp)
                    num_temp = ''
                    break
            else:
                if num_temp != '':
                    file_num = int(num_temp)
                    num_temp = ''
                    break
                else:
                    head += text
        if num_temp != '':
            file_num = int(num_temp)
        head = head.lower()
        heappush(sort_q, ((head, file_num, idx), file))
    while sort_q:
        pop = heappop(sort_q)
        answer.append(pop[1])
    return answer
