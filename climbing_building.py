buliding=int(input("enter the number of building"))
buildhigth=[]
temp=0
k=0
j=1
x=0
blocks=int(input("enter the number of blocks"))
ladders=int(input("enter the number of ladders"))
for i in range(buliding):
    buildhigth.append(int(input("enter the hights of buildungs")))
while k<=buliding:
    if buildhigth[k]<buildhigth[j]:
        temp=buildhigth[j]-buildhigth[k] 
        if temp<=blocks:
            buildhigth[k]=buildhigth[k]+temp
            blocks=blocks-temp                
            temp=0  
            continue     
        elif ladders>=1:             
            buildhigth[k]=buildhigth[k]+temp                    
            ladders-=1                
            temp=0  
            continue                
        elif temp>blocks and ladders==0 and temp==0:
            inde=(buildhigth[j])#element
            x=buildhigth.index(inde)
            print(x-1,)
            break
        else:        
            inde=(buildhigth[j])#element
            x=buildhigth.index(inde)
            print(x-1,)
            break                   
    k+=1            
    j+=1    
    if j==len(buildhigth):
        print(buildhigth[j-1])
        break
