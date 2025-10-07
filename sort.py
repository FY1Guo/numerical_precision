from num import HPNumber
import numpy as np
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

def merge_sort(arr):
    def merge(left, mid, right):
        left_part = arr[left:mid]
        right_part = arr[mid:right]
        i = 0 #left half index
        j = 0 #right half index
        k = left #write index on arr
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i = i + 1
            else:
                arr[k] = right_part[j]
                j = j + 1
            k = k + 1
        while i < len(left_part):
            arr[k] = left_part[i]
            i = i + 1
            k = k + 1
        while j < len(right_part):
            arr[k] = right_part[j]
            j = j + 1
            k = k + 1
    def sort(left, right):
        if right - left > 1:
            mid = (left + right) // 2
            sort(left, mid)
            sort(mid, right)
            merge(left, mid, right)
    sort(0, len(arr)) #exlusive of end point
    return arr

N_list = np.arange(1000000, step = 500)
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
