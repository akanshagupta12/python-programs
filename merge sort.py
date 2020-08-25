def merge(l,r,arr):
    nl=l.length;
    nr=r.length;
    i=0,j=0,k=0;
    while(i<nl and j<nr):
        if(l[i] < r[j]):
            arr[k]=l[i];
            i+=1;
            k+=1;
        else:
            arr[k]=r[j];
            j+=1;
            k+=1;
    while(i<nl):
        arr[k]=l[i];
        i+=1;
        k+=1;
    while(r<nr):
        arr[k]=r[j];
        j+=1;
        k+=1;
def mergesort(arr):
    n=arr.length;
    if(n<2):
        return ;
    mid=n/2;
    for(int i=0;i<mid;i++):
        left[i]=arr[i];
    for (int i=mid;i < n;i++):
        right[i] = arr[i];
    mergesort(left);
    mergesort(right);
    merge(left,right,arr);
arr=[]
n=int(input("enter the size of array"))
for i in range (0,n):
    arr.append(int(input()));
mergesort(arr);
print(*arr);


