T = int(input())
for _ in range(T):
	arr = input()
	n_strike = 0
	sum=0
	for i in range(len(arr)):
		answer = arr[i]
		if answer=='O':
			n_strike+=1
		else:
			n_strike=0
		sum+=n_strike
	print(sum)