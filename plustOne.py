def plusOne(digits):
        return list(map(int,str(int("".join(map(str,digits)))+1)))

def plusOne1(digits):
    if digits[-1]+1<10:
        return digits[:-1]+[digits[-1]+1]
    elif len(digits)==1 and digits[0]==9:
        return[1,0]
    else:
        print("last digit create carrier")
        c=1
        digits[-1]=0
        for d in range(len(digits)-2,0,-1):
            print('d',d,'current digit',digits[d])
            if (digits[d]+c)>=10:
                digits[d]=0
                c=1
                print('carriers', digits)
            else:
                c=0
                print('no carriers')
                return digits
        if len(digits)>1 and c==1 and digits[0]==9:
            print("first digit is 9")
            return [1,0]+digits[1:]
        else:
            return digits

a=[9]
t=plusOne1(a)
