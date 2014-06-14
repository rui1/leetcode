class Point:
 def __init__(self, a=0, b=0):
     self.x = a
     self.y = b
a=[]
a.append(Point(0,0))
a.append(Point(1,1))
a.append(Point(1,-1))

b=[]
b.append(Point(2,3))
b.append(Point(3,3))
b.append(Point(-5,3))


c=[]
c.append(Point(0,0))
c.append(Point(1,1))
c.append(Point(0,0))
test=[(-4,-4),(-8,-582),(-3,3),(-9,-651),(9,591)]
d=[]

    d.append(Point(i[0],i[1]))
def maxPoints(points):
    if len(points)<=2:
        return len(points)
    else:
        mx = 0
        for i in range(len(points)-1):
            hs = {}
            same =0
            for j in points[i+1:]:
                tmpKey = fraction(j.y-points[i].y,j.x-points[i].x)
                #print("(",points[i].x,points[i].y,")",j.x,j.y)
                if j.y==points[i].y and j.x==points[i].x:
                    #print(same)
                    same+=1
                elif tmpKey in hs:
                    hs[tmpKey]+=1
                else:
                    hs[tmpKey]=2
            print(hs,same)
            if len(hs)==0:
                mx = max(mx, same+1)
            else:
                mx=max(mx, max(hs.values())+same)
            print('mx',mx)
        return mx
def fraction(x,y):
    if x==0 or y==0:
        return (0,0)
    else:
        f=gcd(x,y)
        return(x/f,y/f)
def gcd(x,y):
    while y!=0:
        x,y = y, x%y
    return x
