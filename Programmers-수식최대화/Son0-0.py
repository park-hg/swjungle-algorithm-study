from itertools import permutations


def solution(expression):
    answer = 0

    flist = []
    temp_str = ''

    for a in expression:
        if not a.isdigit():
            flist.append(temp_str)
            flist.append(a)
            temp_str = ''
        else:
            temp_str += a
    if temp_str:
        flist.append(temp_str)

    max_value = 0
    for c in list(permutations(['*', '+', '-'], 3)):
        temp = flist[:]
        for op in c:
            while op in temp:
                idx = temp.index(op)
                num1 = int(temp[idx - 1])
                num2 = int(temp[idx + 1])

                if op == '*':
                    temp[idx - 1] = ''
                    temp[idx] = num1 * num2
                    temp[idx + 1] = ''
                elif op == '+':
                    temp[idx - 1] = ''
                    temp[idx] = num1 + num2
                    temp[idx + 1] = ''
                else:
                    temp[idx - 1] = ''
                    temp[idx] = num1 - num2
                    temp[idx + 1] = ''
                temp = [a for a in temp if a != '']

        max_value = max(max_value, abs(sum(temp)))

    return max_value
