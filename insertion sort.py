arr=[]
n=int(input("enter the size of array"))
for i in range (0,n):
    arr.append(int(input()));
for j in range (1,n):
    value=arr[j]
    hole=j
    while(hole>0 and  arr[hole-1]>value):
        arr[hole]=arr[hole-1]
        hole-=1
    arr[hole]=value
print(*arr)