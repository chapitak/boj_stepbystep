test_num = int(input())
for _ in range(test_num):
    input_list = list(map(int, input().split()))
    population = input_list[0]
    scores = input_list[1:]
    average = sum(scores)/population
    over_average = 0
    for i in range(population):
        if scores[i] > average:
            over_average += 1
    print('{}%'.format(format((over_average/population)*100, ".3f")))


