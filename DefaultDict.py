
a , b = map(int, input().split())
words_a=[input() for _ in range(a)]
words_b=[input() for _ in range(b)]

for i in words_b:
    for index, char in enumerate(words_a):
        if i==char:
            print(index+1, end=' ')
        elif i not in words_a:
            print('-1')
    print()
        # if i not in words_a :
        #     print("-1")
    
        



        


