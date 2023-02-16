import sys
import json
import time
import matplotlib.pyplot as plt


sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high



# Load the JSON file
with open("ex2.json", "r") as file:
    inputs = json.load(file)

# Measure the time taken by the code to sort each input
timing_results = []

for input in inputs:
    start_time = time.time()
    func1(input, 0, len(input)-1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    timing_results.append((len(input), elapsed_time))

# Plot the timing results
x = [result[0] for result in timing_results]
y = [result[1] for result in timing_results]
plt.plot(x, y)
plt.xlabel("Size of input")
plt.ylabel("Elapsed time (seconds)")
plt.show()
