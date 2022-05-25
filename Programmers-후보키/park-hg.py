def solution(relations):
    r = len(relations)
    c = len(relations[0])
    
    candidate = []
    for bit in range(1<<c):
        S = set()
        for rel in relations:
            subset = ''
            for i in range(c):
                if bit & (1<<i):
                    subset += rel[i]
            S.add(subset)
        if len(S) == r:
            candidate.append(bit)

    uniqueness = [True]*len(candidate)
    for i in range(len(candidate)-1):
        if uniqueness[i]:
            for j in range(i+1, len(candidate)):
                if candidate[i] & candidate[j] == candidate[i]:
                    uniqueness[j] = False

    return sum(uniqueness)