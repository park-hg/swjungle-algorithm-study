def solution(relations):
    r = len(relations)
    c = len(relations[0])
    
    uniqueness = []
    for bit in range(1<<c):
        S = set()
        for rel in relations:
            subset = ''
            for i in range(c):
                if bit & (1<<i):
                    subset += rel[i]
            S.add(subset)
        if len(S) == r:
            uniqueness.append(bit)

    minimnality = [True]*len(uniqueness)
    for i in range(len(uniqueness)-1):
        if minimnality[i]:
            for j in range(i+1, len(uniqueness)):
                if uniqueness[i] & uniqueness[j] == uniqueness[i]:
                    minimnality[j] = False

    return sum(minimnality)