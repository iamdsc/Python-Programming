#Author:
#Dilpreet Singh Chawla
#Indian Institute of Information Technology Kalyani

#Sorting Algorithms in python

#Modified Bubble Sort - O(n^2)

def bubblesort(l):
    n=len(l)
    for i in range(n):
        f=0
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                f=1
                (l[j],l[j+1])=(l[j+1],l[j])
        if f==0:                                      #For best case of already sorted it becomes O(n)
            break


#Selection Sort - O(n^2)

def selectionsort(l):
    n=len(l)
    for i in range(n):
        minpos=i
        for j in range(i,n):
            if l[j]<l[minpos]:
                minpos=j
        (l[i],l[minpos])=(l[minpos],l[i])

        
#Insertion Sort - O(n^2)

def insertionsort(l):
    n=len(l)
    for i in range(n):
        pos=i
        while pos>0 and l[pos]<l[pos-1]:     #For Best Case of already sorted it becomes O(n)
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos-=1


#Merge sort - O(n*log n)
            
def merge(A,B):     #Merging two sorted lists A[0:m] and B[0:n]
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)         #To store current positions in A and B
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j+=1
        elif j==n:
            C.append(A[i])
            i+=1
        elif A[i]<=B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1
    return C

def mergesort(A,l,r):
    if r-l<=1:          #Base Case
        return(A[l:r])
    else:
        mid=(l+r)//2
        #Recursive Call
        L=mergesort(A,l,mid)
        R=mergesort(A,mid,r)
        return (merge(L,R))


#Quicksort - O(n*log n)
#In worst case of already sorted time complexity becomes O(n^2)
    
def quicksort(A,l,r):
    if r-l<=1:
        return
    low=l+1
    for high in range(l+1,r):          
        if A[high]<=A[l]:
            (A[low],A[high])=(A[high],A[low])
            low=low+1
    (A[l],A[low-1])=(A[low-1],A[l])
    quicksort(A,l,low-1)
    quicksort(A,low,r)

    
