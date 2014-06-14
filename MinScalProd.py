def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results

def get_Case(content,n):
    case = []
    start = 3*n-2
    N = list(map(int,content[start].replace('\n','').split(' ')))
    x = list(map(int,content[start+1].replace('\n','').split(' ')))
    y = list(map(int,content[start+2].replace('\n','').split(' ')))
    case.append(N)
    case.append(x)
    case.append(y)
    return case



def MinScal(case):
    n = case[0][0]
    x = case[1]
    y = case[2]
    prod = 0
    for i in range(n):
        prod += max(x)*min(y)
        x.pop(x.index(max(x)))
        y.pop(y.index(min(y)))
    return prod

def run(content, size):
    out_f =open('MinScal'+size+'output.txt','w', encoding='utf-8')
    #open('C:\Users\mc31141\Desktop\miscellanea'+size+'output.txt','w',encoding='utf-8')

    for i in range(1,int(content[0])+1):
        case = get_Case(content,i)
        result = "Case #"+str(i)+": "+str(MinScal(case))
        #print (results)
        out_f.write(result+'\n')

content = read_in('MinScalProd_Small.in')
content1 = read_in('MinScalProd_Large.in')
run(content, 'small')
run(content1, 'large')
