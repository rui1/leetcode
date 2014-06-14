def romanToInt(s):
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    pre = s[0]
    result = nums[pre]
    for i in s[1:]:
        if nums[i]>nums[pre]:
            result+=nums[i]-2*nums[pre]
        else:
            result+=nums[i]
        pre =i
        print(result,pre)
    return result
nums = {'M':1000,'CM':900, 'D':500, 'CD':400,'C':100,'XC':90,'L':50, 'XL':40,'X':10,'IX':9, 'V':5,'IV':4, 'I':1}

romanNumeralMap = (('M',  1000), 
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
def toRoman(n):
    """convert integer to Roman numeral"""
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:      
            result += numeral
            n -= integer
            print(result,n)
    return result
def toRoman1(n):
    """convert integer to Roman numeral"""
    result = ""
    for i in nums:
        print(i)
        while n >= nums[i]:      
            result += i
            n -= nums[i]
            print(result,n)
    return result
