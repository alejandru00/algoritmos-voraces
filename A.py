
height = list(map(int, input().split()))

n = len(height)
i = 0
j = n - 1
max_area = 0

while i < j:
    width = min(height[i], height[j])
    area = width * (j - i)
    max_area = max(max_area, area)

    if height[i] < height[j]:
        i += 1
    else:
        j -= 1

print(max_area)
