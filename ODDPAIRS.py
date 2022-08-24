# for i in range(int(input())):
#     n = int(input())
#     #for i in range(1,(10**9)+1):
#     count_b = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             count_b = count_b  + 2
#     print(count_b)    


# the number of odd pairs formula = n(n/2) wher bothe the n and n/2 should be integers 
for i in range(int(input())):
    n = int(input())
    out = n*n//2
    print(out)
