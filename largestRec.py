def lRec(height):
    if len(height)==0:
        return 0
    else:
        stack = []
        area = 0
        i=0
        while i <len(height):
            if len(stack)==0 or height[i] >height[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                tmp =stack[-1]
                stack.pop()
                if len(stack)==0:
                    area = max(area, height[tmp]*i)
                else:
                    area = max(area, height[tmp]*(i-stack[-1]-1)) 
            #print(stack)
        while len(stack) !=0:
            tmp =stack[-1]
            stack.pop()
            if len(stack)==0:
                area = max(area, height[tmp]*i)
            else:
                area = max(area, height[tmp]*(i-stack[-1]-1)) 
        return area
                
            
            
#height=[1,2,3]

def lRec_kadone_Wrong(height):
    if len(height)==0:
        return 0
    else:
        cur= best =start=0
        h = height[0]
        for i in range(len(height)):
            if height[i]<h:
                h = height[i]
            #cur =min(height[start:i+1])*(i+1-start)
            cur = h *(i+1-start)
            cur = max(cur,height[i])
            if cur == height[i]:
                start = i
                h = height[i]
            best = max(cur,best)
            print(height[i],cur, best, start)
        return best



height =[2,1,5,6,2,3]
height=[4,2]
lRec(height)
#height = [1,2,3,4,5]
