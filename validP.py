def isP(s):
    if len(s)==0:
        return True
    else:
        ss = ''.join([x for x in s.lower() if x in '1234567890abcdefghijklmnopqrstuvwxyz'])
        l = len(ss)
        mid =l//2
        if l%2:
            left = ss[:mid+1]
            rev = left[::-1][1:]
            return ss[mid+1:]==rev
        else:
            left = ss[:mid]
            rev = left[::-1]
            return ss[mid:]==rev



s='a man, a plan, a canal: Panama'
s="1a2"
'''ss = ''.join([x for x in s.lower() if x in 'abcdefghijklmnopqrstuvwxyz'])
l = len(ss)
mid =l//2
if l%2:
    left = ss[:mid+1]
    rev = left[::-1][1:]
    t=ss[mid+1:]==rev
else:
    left = ss[:mid]
    rev = left[::-1]
    t=ss[mid:]==rev'''
