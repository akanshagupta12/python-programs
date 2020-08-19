a=[]
n=int(input("enter the size of array"))
for i in range(0,n):
    a.append(int(input()));
b = [];
for j in range(0, n):
    b.append(0);
k=10;
def countSort(a,k,n,b){
    c=[];
    for k in range(0,k):
            c.append(0);
    for c in range(0,n):
        c[a[c]]+=1;
    for g in range(1,k):
        c[g]=c[g]+c[g-1];
    for j in range(n-1,-1):
        b[c[a[j]]-1]=a[j];
        c[a[j]]-=1;
    print(*b);
}
countSort(a,k,n,b);