import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    else:
        total = 0
        max_num = 0
        n_list = []
        for i in range(a) :
            n_list.append(int(input()))
        max_num = max(n_list)

        for i in range(a+1) :
            if  (a-1-i) > 0 :
                print("a-1-i :", a-1-i)
                print("a-1 :", a -1)
                num = (a-1-i) / (a - 1)        #i+1 ~ a+1 까지 , 제일 맥스 값 분에 현재 크기
                if n_list[i] == 0 :
                    total += 0
                else:
                    total += num * (b/n_list[i])*(n_list[i]/max_num)

        total += 1 / pow(10, len(n_list)-1)  #축과 글자
        print(total)
