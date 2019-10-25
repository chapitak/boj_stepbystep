test_num = int(input())
sum_new_test_points = 0
test_points = list(map(int, input().split()))
max_points = max(test_points)
for i in range(test_num):
    new_test_points = (test_points[i]/max_points)*100
    sum_new_test_points += new_test_points

#print(sum_new_test_points)
print(sum_new_test_points/test_num)