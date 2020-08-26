def radixSort(arr):
    maximum=max(arr)
    n=1;
    while maximum//n > 0:
        countingsort(arr,n)
        n=n*10
def countingsort(arr,p):
    n=len(arr)
    res=[0]*n;
    c=[0]*10;
    for i in range(0,n):
        temp=arr[i]//p
        c[temp%10]+=1
    for g in range(1, 10):
        c[g] = c[g] + c[g - 1];
    for j in range(n - 1, -1,-1):
        temp = arr[j] // p
        res[c[temp%10]-1]=arr[j]
        c[temp%10]-=1
    for i in range(0,n):
        arr[i]=res[i]
arr=[]
n=int(input("enter the size of array"))
for i in range(0,n):
    arr.append(int(input()));
radixSort(arr)
print(*arr)