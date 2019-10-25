test_num = int(input())
#made_str = []
for _ in range(test_num):
    multiply_num, target_str = input().split()
    multiply_num = int(multiply_num)
    target_str = str(target_str)
    for i in range(len(target_str)):
        print(target_str[i]*multiply_num, end='')
        # made_str += target_str[i]*multiply_num
    print('')


