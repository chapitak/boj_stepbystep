a, b = map(str, input().split())
reversed_a = 0
reversed_b = 0

for i in range(len(a)):
    reversed_a += int(a[i])*pow(10,i)
for i in range(len(b)):
    reversed_b += int(b[i])*pow(10,i)    
print(max([reversed_a, reversed_b]))