# 하노이탑 알고리즘 어떻게 짜나? ㅠ 
def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else: 
        hanoi(disk-1, start, end, mid) #이건 첫쨰칸에서 중간 칸으로 옮기는 것이다. 
        print(start, end) # 이건 가장 큰 판을 끝 칸으로 옮기는 것. 
        hanoi(disk-1, mid, start, end) # n-1개의 중간 칸에 있는 것을 끝칸으로 옮기는 것. 


def get_times(n):
    if n == 1:
        return 1
    else: 
        return get_times(n-1)*2 + 1 
disnk_number = int(input())
print(get_times(disnk_number))
hanoi(disnk_number,1,2,3)         