x = input()
x = int(x)
a = x%2==0
b = 4<x<=12
if a and b:
    result_a = 1
else:
    result_a = 0
if a or b:
    result_uim = 1
else:
    result_uim = 0
if a !=b :
    result_b = 1
else:
    result_b = 0
if not (a or b):
    result_zhengmei = 1
else:
    result_zhengmei = 0
print(result_a,result_uim,result_b,result_zhengmei)

    

       
   


    
