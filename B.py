
hunger = list(map(int, input().split()))

n = len(hunger)
caramelos = n

for i, current in enumerate(hunger):
    if i == 0:
        next_hunger = hunger[i + 1]
    elif i == n - 1:
        next_hunger = hunger[i - 1]
    else:
        next_hunger = max(hunger[i + 1], hunger[i - 1])

    if current > next_hunger:
        caramelos += 1

print(caramelos)
