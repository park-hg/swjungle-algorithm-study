# 자꾸 틀려서 지난 번에 푼 것을 보고 풀었습니다
from collections import defaultdict

def solution(info, query):
    # print(info)
    dic = {}
    items = ['cpp', 'java', 'python', 'lan',  'backend', 'frontend', 'job', 'junior', 'senior', 'rank', 'chicken', 'pizza', 'food']
    for i, item in enumerate(items):
        dic[item] = i
    # print(dic)
    data_dic = defaultdict(list)

    for data in info:
        data = data.split()
        score = int(data[4])
        data = data[:-1]
        num = 0
        for i in [dic[data[0]], dic['lan']]:
            for j in [dic[data[1]], dic['job']]:
                for k in [dic[data[2]], dic['rank']]:
                    for l in [dic[data[3]], dic['food']]:
                        data_dic[(i, j, k, l)].append(score)
    for d in data_dic:
        data_dic[d].sort()
    
    ret = []
    for data in query:
        data = data.split(" and ")
        tmp = data[3].split()
        data[3] = tmp[0]
        num = 0
        if data[0] == "-": data[0] = 'lan'
        if data[1] == "-": data[1] = 'job'
        if data[2] == "-": data[2] = 'rank'
        if data[3] == "-": data[3] = 'food'
        
        num = (dic[data[0]], dic[data[1]], dic[data[2]], dic[data[3]])
        target = int(tmp[1])
        
        start = 0
        end = len(data_dic[num])
        while(start < end):
            mid = (start+end) // 2
            if data_dic[num][mid] >= target:
                end = mid
            else:
                start = mid + 1
        
        ret.append(len(data_dic[num]) - start)

    return ret
