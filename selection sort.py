def selectionSort(arr):
    for j in range(0,n-1):
        min=j;
        for k in range(j+1,n):
            if(arr[k]<arr[min]):
                min=k;
        temp=arr[j];
        arr[j]=arr[min];
        arr[min]=arr[j];
    print(*arr);
arr=[]
n=int(input("enter the size of array"))
for i in range (0,n):
    arr.append(int(input()));
bubbleSort(arr);