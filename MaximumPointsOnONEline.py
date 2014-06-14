class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self,points):
        if len(points)<=2:
            return len(points)
        else:
            mx = 0
            for i in range(len(points)-1):
                hs = {}
                same =0
                for j in points[i+1:]:
                    tmpKey = self.fraction(j.y-points[i].y,j.x-points[i].x)
                    #print("(",points[i].x,points[i].y,")",j.x,j.y)
                    if j.y==points[i].y and j.x==points[i].x:
                        #print(same)
                        same+=1
                    elif tmpKey in hs:
                        hs[tmpKey]+=1
                    else:
                        hs[tmpKey]=2
                if len(hs)==0:
                    mx = max(mx, same+1)
                else:
                    mx=max(mx, max(hs.values())+same)
            return mx
    def fraction(self,x,y):
        if x==0 or y==0:
            return (0,0)
        else:
            f=self.gcd(x,y)
            return(x/f,y/f)
    def gcd(self,x,y):
        while y!=0:
            x,y = y, x%y
        return x
