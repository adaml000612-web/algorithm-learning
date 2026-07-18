x = input() 
x = int(x)
if x%2==0 and 4<x<=12:
     result_a = 1
else: 
     result_a = 0 
if x%2==0 or 4<x<=12:
     result_uim  = 1
else:  
     result_uim = 0 
if (x%2==0 and not 4<x<=12) or (4<x<=12 and           not x%2==0): 
     result_b = 1
else: 
     result_b = 0
if not (x%2==0 or 4<x<=12):
     result_zhengmei = 1
else:  
     result_zhengmei = 0
print(result_a,result_uim,result_b, result_zhengmei) 
       
   


    
