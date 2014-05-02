def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    return results
def get_Case(content,n):
    return [list(map(int,content[n*2-1].replace('\n','').split(" "))),list(map(int,content[n*2].replace('\n','').split(" ")))]

def solver(case):
    [D,I,M,N]=case[0]
    nm = case[1]
    cost=0
    return cost



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
