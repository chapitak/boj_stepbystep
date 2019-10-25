def makenum(constructor: int):
    #madenum = constructor + constructor//10 + constructor%10
    full_constructor = constructor
    for i in range((len(str(constructor)))):
        full_constructor += int(str(constructor)[i])
    return full_constructor

made_number_list = []
for i in range (1, 10000):
    made_number_list.append(makenum(i))
self_number = set(range(1, 10000)) - set(made_number_list)
self_number_copied = list(self_number).copy()
self_number_copied.sort()
print(*self_number_copied, sep='\n')
#print(*made_number_list, sep='\n')

