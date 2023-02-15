def func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    result = func(n-1, memo) + func(n-2, memo)
    memo[n] = result
    return result
