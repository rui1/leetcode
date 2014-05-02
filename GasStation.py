def canCompleteCircuit(self, gas, cost):
    start = 0
    tank =0
    gasNeeded=0
    for i in range(0,len(gas)):
        tank +=gas[i]-cost[i]
        if tank+gas[i]-cost[i]<0:
            start =i+1
            gasNeeded-=tank
            tank = 0
    if tank<gasNeeded:
        return -1
    else:
        return start
