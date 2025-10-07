from num import HPNumber
import numpy.random as rand
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


N_list = range(1000000, step = 500)
bubble_times = []
merge_times = []

for N in N_list:
    a_list = rand.randint(int(-1e10), int(1e10), size = N)
    b_list = rand.randint(int(-1e10), int(1e10), size = N)
    number_list = [HPNumber(a_list[i], b_list[i]) for i in range(N)]
    bubble_times.append(timeit.timeit('bubble_sort(number_list)', number = 100))
    merge_times.append(timeit.timeit('merge_sort(number_list)', number = 100))
    
plt.plot(N_list, bubble_times, label = "Bubble sort")
plt.plot(N_list, merge_times, label = "Merge sort")
plt.legend()
plt.show()
