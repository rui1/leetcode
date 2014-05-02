def firstMissingPositive(self, A):
    if len(A)==0:
        return 1
    else:
        for i in range(1,len(A)+2):
            if i not in A:
                return i  
