input_string = input()
call_time = 0
for c in input_string:
    if c in ['A', 'B', 'C']:
        call_time += 3
    if c in ['D', 'E', 'F']:
        call_time += 4
    if c in ['G', 'H', 'I']:
        call_time += 5
    if c in ['J', 'K', 'L']:
        call_time += 6
    if c in ['M', 'N', 'O']:
        call_time += 7        
    if c in ['P', 'Q', 'R', 'S']:
        call_time += 8
    if c in ['T', 'U', 'V']:
        call_time += 9
    if c in ['W', 'X', 'Y', 'Z']:
        call_time += 10
print(call_time)