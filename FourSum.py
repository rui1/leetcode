import itertools
def fourSum(nums, target):
    ht={}
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            tmpKey = nums[i]+nums[j]
            tmpList = [i,j]
            if tmpKey in ht and tmpList not in ht[tmpKey]:
                ht[tmpKey].append(tmpList)
            elif tmpKey not in ht:
                ht[tmpKey]=[tmpList]
    #tmpht = {psb:ht[psb] for psb in ht if psb <=target}
    print(ht,'\n')
    output=[]
    for k in ht:
        ab = ht[k]
        if target-k in ht:
            cd = ht[target-k]
        else:
            continue
        for pr1 in ab:
            for pr2 in cd:
                if len(set(pr1+pr2))==4:
                    tmp = [nums[i] for i in pr1+pr2]
                    tmp.sort()
                    if tmp not in output:
                        output.append(tmp)
                    else:
                        continue
    return output

'''output = []
tmpht = {2: [[0, 1]], 3: [[0, 2], [1, 2]], 4: [[0, 3], [1, 3]]}
target = 6
for k in tmpht:
    ab = tmpht[k]
    if target-k in tmpht:
        cd = tmpht[target-k]
        print(ab,cd)
    else:
        continue
    for pr1 in ab:
        for pr2 in cd:
            if len(set(pr1+pr2))==4:
                tmp = [nums[i] for i in pr1+pr2]
                tmp.sort()
                if tmp not in output:
                    output.append(tmp)
                else:
                    continue '''       
            
            
    
