def read_in(filename):
    a_file = open(filename, encoding='utf-8')
    results = a_file.readlines()
    #print lines
    return results
def get_Case(content,n):
    return [list(content[n*2-1].replace('\n','').split(" ")),list(content[n*2].replace('\n','').split(" "))]
def solver(case):
    [D,I,M,N]=list(map(int, case[0]))
    seq = list(map(int, case[1]))
    stats = []
    for i in seq:
        if len(stats)==0:
            stats.append({})
        
    
def run(filename,size):
    out_f =open('MakeSmooth'+size+'output.txt','w', encoding='utf-8')
    content = read_in(filename)
    caseN = int(content[0].replace('\n',''))
    print(caseN)
    for i in range(1,caseN+1):
        case = get_Case(content, i)
        result = "Case #"+str(i)+": "+str(solver(case))
        out_f.write(result+'\n')

content = read_in("MakeItSmooth_Small.in")
case = get_Case(content,1)
