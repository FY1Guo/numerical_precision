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

N_list_bubble = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200,300,400, 500]
N_list_merge = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200,300,400, 500, 750, 1000, 1500, 2000, 2500, 5000, 6000, 7000, 8000, 9000, 10000]
bubble_times = []
merge_times = []

for N in N_list_bubble:
    total_time_bubble = 0
    print(N)
    for i in range(5):
        a_list = rand.randint(int(-10), int(10), size = N)
        b_list = rand.randint(int(-2), int(2), size = N)
        number_list = [HPNumber(a_list[i], b_list[i]) for i in range(N)]
        total_time_bubble += timeit.timeit("bubble_sort(number_list)", globals = globals(), number = 1)
    bubble_times.append(total_time_bubble/5)
    
    
for N in N_list_merge:
    total_time_merge = 0
    print(N)
    for i in range(5):
        a_list = rand.randint(int(-10), int(10), size = N)
        b_list = rand.randint(int(-2), int(2), size = N)
        number_list = [HPNumber(a_list[i], b_list[i]) for i in range(N)]
        total_time_merge += timeit.timeit("merge_sort(number_list)", globals = globals(),number = 1)
    merge_times.append(total_time_merge/5)

plt.title("Bubble sort")
plt.plot(N_list_bubble, bubble_times)
plt.xlabel("List length")
plt.ylabel("Time")
plt.show()

plt.clf()
plt.title("Merge sort")
plt.plot(N_list_merge, merge_times)
plt.xlabel("List length")
plt.ylabel("Time")
plt.show()

plt.clf()
plt.title(r"Comparing Bubble sort to $N^2$")
plt.plot(N_list_bubble, np.array(bubble_times)/np.array(N_list_bubble)**2)
plt.xlabel(r"$N$")
plt.ylabel(r"Time/$N^2$")
plt.show()

plt.clf()
plt.title(r"Comparing merge sort to $N\ln N$")
plt.xlabel(r"$N$")
plt.ylabel(r"Time/$N\ln N$")
plt.plot(N_list_merge, np.array(merge_times)/(np.array(N_list_merge)*np.log(np.array(N_list_merge))))
plt.show()
