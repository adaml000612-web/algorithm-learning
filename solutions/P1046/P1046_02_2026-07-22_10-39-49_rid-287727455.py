x = list(map(int,input().split()))
TaoTao = int(input())
n = 0
for i in range(len(x)):
    if x[i] <= TaoTao + 30:
       n = n + 1
print(n)
    
    

    
