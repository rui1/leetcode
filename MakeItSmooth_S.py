def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    return results
def get_Case(content,n):
    return [list(map(int,content[n*2-1].replace('\n','').split(" "))),list(map(int,content[n*2].replace('\n','').split(" ")))]

def solver(case):
    [D,I,M,N]=case[0]
    nm = case[1]
    count=0
    return count


def solver_p(case):
    [D,I,m,N]=case[0]
    data = case[1]    
    n = len(data)
    tab = [0] * 256
    otab = [0] * 256
    for i in range(*[0,n]):
        otab, tab = tab, otab
        for j in range(*[0,256]):
            cur = otab[j] + D
            base = abs(data[i] - j)
            if cur > base:
                for k in range(*[0,256]):
                    if m == 0 and k != j:
                        continue
                    new = otab[k]
                    if k < j:
                        new += (j-k - 1) // m * I
                    elif k > j:
                        new += (k-j - 1) // m * I
                    if cur > base+new:
                        cur = base+new
            tab[j] = cur
    return min(tab[i] for i in range(*[0,256]))
def run(filename,size):
    out_f =open('MakeItSmooth'+size+'output.txt','w', encoding='utf-8')
    content = read_in(filename)
    caseN = int(content[0].replace('\n',''))
    print(caseN)
    for i in range(1,caseN+1):
        case = get_Case(content, i)
        count = str(solver_p(case))
        result = "Case #"+str(i)+": "+count

        out_f.write(result+'\n')


run("MakeItSmooth_Small.in","Small")
run("MakeItSmooth_Large.in","Large")

