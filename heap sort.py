def heapify(arr,n,i):
    largest=i;
    l=2*i+1;
    r=2*i+2;
    if(l<n and arr[l]>arr[largest]):
        largest=l;
    if(r<n and arr[r]>arr[largest]):
        largest=r;
    if(largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest];
        heapify(arr,n,largest);
def sort(arr):
    n=arr.length;
    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i);
    for j in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i];
        heapify(arr,i,0);
arr=[]
n=int(input("enter the size of array"))
for i in range (0,n):
    arr.append(int(input()));
sort(arr);
print(*arr);