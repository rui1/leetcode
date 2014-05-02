def Maxi1s(arr):
    mx =0
    j=0
    for i in range(len(arr)):
        tmp = arr[i].count(1)
        if tmp>mx:
            mx=tmp
            j=i
    return j

def Maxi1s_2(arr):
    mx = 0
    if 0 not in arr[0]:
        j = -1
    else:
        j = arr[0].index(0)-1
    if j==-1:
        j = len(arr[0])-1
    for i in range(len(arr)):
        while(j>=0 and arr[i][j]==1):
            j-=1
            mx = i
    return mx

arr=[[0,0,0,1],[0, 1, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
        
