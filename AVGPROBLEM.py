for i in range(int(input())):
    t = input().split()
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    avg = (a + b)/2
    if avg > c:
        print('YES')
    else:
        print('NO')
