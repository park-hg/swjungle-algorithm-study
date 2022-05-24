# 26. 금과 은 운반하기(Programmers)
def solution(a, b, g, s, w, t):
    answer = -1
    goal = [0, 0]
    min_time = 0

    while True:
        for n in range(len(t)):
            print('goal ', goal)
            if goal[0] < a and g[n]:
                goal[0] += w[n]
                g[n] -= w[n]
            elif goal[1] < b and s[n]:
                goal[1] += w[n]
                s[n] -= w[n]
            if goal[0] >= a and goal[1] >= b:
                min_time += t[n]
                print('min time', min_time)
                return answer
            else:
                min_time += (t[n] * 2)
        print('min time', min_time)
    return answer

solution(10,10,[100],[100],[7],[10])