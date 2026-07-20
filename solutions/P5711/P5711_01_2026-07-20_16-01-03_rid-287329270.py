x = input()
x = int(x)
a = x%4==0
b = x%100==0
c = x%400==0
if (a and not b) or c:
   result_run = 1
else:
   result_run = 0
print(result_run)
