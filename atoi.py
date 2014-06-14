class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        x = 1
        found = False
        ret = ''
        if len(str)==0:
            return 0
        else:
            if str[0] =='-' or str[0] =='+':
                start = 1
            else:
                start = 0
            for x in range(start+1,len(str)+1):
                if not str[start:x].isdigit():
                    found = True
                    break
            if found:
                ret = str[:x-1]
            else:
                ret = str[:x]
            try:
                t = int(ret)
                if t >=0:
                    return min(t,2147483647)
                else:
                    return max(t, -2147483648)
            except:
                return 0
test = Solution()
#print test.atoi('1')
print test.atoi('+-123.fgeaq')
