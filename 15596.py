def solve(a: list):
    list_sum = 0
    for i in range(len(a)):
        list_sum += a[i]
    return list_sum

print(solve([1, 2, 3]))