melody = list(map(int, input().split()))

melody_sorted = melody.copy()
melody_sorted.sort()
melody_sorted_reverse = melody.copy()
melody_sorted_reverse.sort(reverse=True)

if melody_sorted == melody:
    print('ascending')
elif melody_sorted_reverse == melody:
    print('descending')
else: 
    print('mixed')