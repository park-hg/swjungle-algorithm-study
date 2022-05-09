def solution(n, k, cmd):
    numbers = list(range(n))
    idx = k
    z = []
    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            k -= int(c[1])
        elif c[0] == 'D':
            k += int(c[1])
        elif c[0] == 'C':
            z.append((k, numbers[k]))
            numbers.remove(numbers[k])
            if k >= len(numbers):
                k = len(numbers)-1
        elif c[0] == 'Z':
            idx, num = z.pop()
            numbers = numbers[:idx] + [num] + numbers[idx:]
            if k > idx:
                k += 1
            
    answer = ['X']*n
    for num in numbers:
        answer[num] = 'O'
            
    return ''.join(answer)