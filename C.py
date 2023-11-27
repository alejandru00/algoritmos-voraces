
nums = list(map(int, input().split()))

n = len(nums)
max_ind = 0

def index(a, n, max_ind):
    for i in range(n):
        if max_ind < i:
            return False
        max_ind = max(max_ind, i + a[i])
    return max_ind >= n - 1

print(index(nums, n, max_ind))