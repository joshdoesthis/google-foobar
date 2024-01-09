def solution(l, t):
    # return early if exact match can be found
    if t in l:
        return [l.index(t), l.index(t)]
    # iterate through all possible sublists
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            s = sum(l[i:j + 1])
            if s == t:
                return [i, j]
            # break early if sum is greater than t
            if s > t:
                break
    return [-1, -1]