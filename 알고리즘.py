import random
import numpy as np
import time

# Median of Medians algorithm (BFPRT)
def select(arr, left, right, k):
    if right - left + 1 <= 5:
        return sorted(arr[left:right+1])[k - 1]

    medians = []
    i = left
    while i <= right:
        sub_right = min(i + 4, right)
        sublist = sorted(arr[i:sub_right + 1])
        medians.append(sublist[len(sublist)//2])
        i += 5

    pivot = select(medians, 0, len(medians) - 1, len(medians) // 2)
    pivot_index = partition(arr, left, right, pivot)

    rank = pivot_index - left + 1
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return select(arr, left, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, right, k - rank)

def partition(arr, left, right, pivot):
    for i in range(left, right + 1):
        if arr[i] == pivot:
            arr[i], arr[right] = arr[right], arr[i]
            break
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

# 시간 측정 함수
def run_experiment(N):
    A = np.random.normal(loc=500, scale=100, size=N).tolist()
    total_time = 0
    for k in range(1, N + 1):
        B = A.copy()
        start = time.time()
        select(B, 0, N - 1, k)
        end = time.time()
        total_time += (end - start)
    avg_time = total_time / N
    return avg_time

# 실험
for N in [100, 1000, 10000]:
    avg_time = run_experiment(N)
    print(f"N={N}, 평균 수행 시간 = {avg_time:.6f}초")
