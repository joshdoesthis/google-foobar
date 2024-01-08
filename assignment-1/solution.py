def solution(data, n):
    # return early if n is not an integer or is not between 0 and 99
    if type(n) != int or n < 0 or n > 99:
        return []
    # return early if data is not a list or is empty or has more than 99 elements
    if len(data) == 0 or len(data) > 99:
        return []
    # return early if data is not a list of integers or has negative integers
    for i in data:
        if type(i) != int or i < 0:
            return []
    # return a list of integers that occur less than or equal to n times
    return [i for i in data if data.count(i) <= n]