def solution(data, n):
    if type(n) != int or n < 0 or n > 99:
        return []
    if len(data) == 0 or len(data) > 99:
        return []
    for i in data:
        if type(i) != int or i < 0:
            return []
    return [i for i in data if data.count(i) <= n]

print(solution([1, 2, 3], 1))