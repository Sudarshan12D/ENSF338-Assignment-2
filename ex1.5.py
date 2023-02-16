import time
import matplotlib.pyplot as plt

def time_func(func, n, *args):
    start = time.time()
    result = func(n, *args)
    end = time.time()
    return end - start

def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

def optimized_func(n, memo):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    result = optimized_func(n-1, memo) + optimized_func(n-2, memo)
    memo[n] = result
    return result


original_times = []
optimized_times = []
for i in range(35):


    original_times.append(time_func(original_func, i))
    optimized_times.append(time_func(optimized_func, i, {}))



plt.plot(range(35), original_times, label = 'Original Function timing')
plt.plot(range(35), optimized_times, label = 'Optimized Function timing')
plt.xlabel("Size of input")
plt.ylabel("Elapsed time (seconds)")
plt.show()




