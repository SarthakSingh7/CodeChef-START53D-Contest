for i in range(int(input())):
    t = input().split()
    w = int(t[0])
    x = int(t[1])
    y = int(t[2])
    z = int(t[3])
    c1 = x+y
    c2 = y+z
    c3 = x+z
    c4 = x+y+z
    l = [x,y,z,c1,c2,c3,c4]
    if w in l:
        print('YES')
    else:
        print('NO')
    
