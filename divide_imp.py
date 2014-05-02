def divide(dividend, divisor):
    if (divisor<0 and dividend>0) or(dividend<0 and divisor>0):
        return -1*self.divide(abs(dividend),abs(divisor))
    if divisor<0 and dividend<0:
        return self.divide(abs(dividend),abs(divisor))
    if dividend == divisor:
        return 1
    if divisor==1:
        return dividend
    if divisor ==-1:
        return -1*dividend
    if dividend < divisor or dividend ==0:
        return 0
    cnt = 0
    while dividend>=divisor:
        tmp =1
        tmpdivisor = divisor
        while (tmpdivisor << 1)<=dividend:
            tmpdivisor=tmpdivisor<<1
            tmp=tmp<<1
        cnt+=tmp
        dividend-=tmpdivisor
        print(cnt,tmp, dividend, tmpdivisor)
    return cnt
 

t=divide(2147483647, 2)
s=divide(13, 2)
