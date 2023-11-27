
def min_swaps(row):
    swaps = 0

    for i in range(0, len(row), 2):
        person = row[i]
        partner = person + 1 if person % 2 == 0 else person - 1

        if row[i + 1] != partner:
            j = row.index(partner)
            row[i + 1], row[j] = row[j], row[i + 1]
            swaps += 1

    return swaps

row =list(map(int, input().split()))

print(min_swaps(row))

