arr=[]
n=int(input("enter the size of array"))
for i in range (0,n):
    arr.append(int(input()));
for j in range(1,n):
    flag=0;
    for k in range(0,n-j):
        if(arr[k]>arr[k+1]):
            temp=arr[k];
            arr[k]=arr[k+1];
            arr[k+1]=temp;
            flag=1;
    if(flag==0):
        break;
print(*arr);
