from collections import defaultdict
from itertools import combinations
import bisect
import pprint

def solution(infos, queries):
  conditions = defaultdict(list)

  # 키 생성 -> 점수 추가
  for info in infos:
    temp_info = info.split()
    info_key = temp_info[:-1]
    info_score = int(temp_info[-1])

    # Combinations를 활용하여 '-'일 경우 추가 
    for i in range(5):
      combi = list(combinations(info_key, i))
      for c in combi:
        temp_key = ''.join(c)
        conditions[temp_key].append(info_score)

  # 점수 오름차순 정렬
  for key in conditions.keys():
    conditions[key].sort()

  answer = []
  for query in queries:
    # query = query.replace('and', ' ')
    query = query.split()
    query_key = query[:-1]
    query_score = int(query[-1])

    for _ in range(3):
      query_key.remove("and")

    # query 안에 '-'있으면 삭제
    while '-' in query_key:
      query_key.remove('-')
    query_key = ''.join(query_key)

    
    idx = bisect.bisect_left(conditions[query_key], query_score)
    answer.append(len(conditions[query_key]) - idx)

  # pprint.pprint(conditions)
  # print(answer)
  return answer
