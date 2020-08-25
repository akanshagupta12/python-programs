def quicksort(arr,start,end):
    if(start<end):
        pindex=partition(arr,start,end);
        quicksort(arr,start,pindex-1);
        quicksort(arr,pindex+1,end);
def partition(arr,start,end):
    pivot=arr[end];
    pindex=start;
    for(int i=start;i<end-1;i++):
        if(arr[i]<pivot):
            arr[i],arr[pindex]=arr[pindex],arr[i];
            pindex+=1;
    arr[pindex],pivot=pivot,arr[pindex];
    return pindex;
arr=[]
n=int(input("enter the size of array"))
start=0;
end=n-1;
for i in range (0,n):
    arr.append(int(input()));
quicksort(arr,start,end);
print(*arr);
