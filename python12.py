num=int(input("enter the number of total dumbles"))
a=[];out1=0;i=0;j=1
for k in range(num):
    a.append(int(input("enter the wight of dumbels")))
a.sort()    
while i<len(a):
    if a[i]==a[j]:
        out1+=1
        a.pop(j)
    i+=1
    j+=1  
    if j==len(a):
        break 
print(out1,"pairs")
