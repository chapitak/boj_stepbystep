input_str = str(input())
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabets:
    try:
        print(input_str.index(i), end=' ')
    except:
        print('-1', end=' ')
