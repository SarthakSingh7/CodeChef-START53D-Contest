for i in range(int(input())):
    x = int(input())
    if x < 300:
        out = 3000
    elif x >= 300:
        out = x * 10
    print(out)    
