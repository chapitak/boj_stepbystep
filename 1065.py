input_number = int(input())
hansoo_num = 0
for i in range(1, input_number+1):
    if i < 100:
        hansoo_num += 1
    elif 100 <= i <= 1000:
        i = str(i)
        if int(i[2])-int(i[1]) == int(i[1])-int(i[0]) :
            hansoo_num += 1
print(hansoo_num)

# 답지않게 어설프게 했다. 어떻게 해야는거지?     