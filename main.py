def addBinary( a: str, b: str) -> str:  
    if len(a) < len(b):
        a, b = b, a
    a = a[::-1]
    b = b[::-1]
    d='0'
    res=''
    lenght=len(b)
    for i in range(len(a)):
        count=0
        if a[i]=='1':
            count+=1    
        if lenght>i and b[i]=='1':
            count+=1    
        if d=='1':
            count+=1    
        if count==3:
            res+='1'
            d='1'
        elif count==2:
            res+='0'
            d='1'
            
        elif count==1:
            res+='1'
            d='0'
        else:
            res+='0'
            d='0'
    if d == '1':
        res+='1'
    return res[::-1]       

 

                    
   
l=addBinary('11', '1001') # 1110
print(l)