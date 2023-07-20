#Input 為 list[0,...,n-1]，將list分為左右兩個子陣列(B & C)後做排序，之後將兩個排序
#完的陣列(B' & C')合併後即完成排序
import math

def merge_sort(A:list, p:int, q:int):
    if p < q:
        m = math.floor( ( p + q ) / 2 )
        merge_sort(A, p, m)    #B
        merge_sort(A, m+1, q)  #C
        merge(A, p, q, m)      #合併

def merge(A:list, p:int, q:int ,m:int):
    L = A[p : m+1] + [99999]
    R = A[m+1 : q+1] + [99999]
    i, j = 0, 0
    for k in range(p, q + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1    

A = [12, 4, 544, 23, 7, 1, 123 ,3]
B = A.copy()
merge_sort(B, 0, len(A)-1)
print(f"Before sorting: {A}")
print(f"After sorting:  {B}")