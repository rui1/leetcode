def sqrt(x):
    if x ==0:
        return 0
    else:
        rt1 = float(x)/2.0
        rt2=1.0/2.0*(float(x)/rt1+rt1)
        while abs(rt2-rt1)>10e-10:
            rt1 = float(rt2)
            rt2=1.0/2.0*(x/rt1+rt1)
        return int(rt2)
