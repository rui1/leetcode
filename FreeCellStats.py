def read_in(filename):
    a_in= open(filename,encoding = 'utf-8')
    results = a_in.readlines()
    return results

def get_Cases(content,n):
    return list(map(int,content[n].replace('\n','').split(' ')))
def solver(case):
    N,Pd,Pg = case
    if Pd != 100 and Pg ==100:
        return "Broken"
    elif 
    return 'Possible'
def run(filename):
    a_out=open(filename+'output.txt',w,encoding='utf-8')
    content = read_in(filename)
    N = int(content[0].replace('\n',''))
    for i in range(1,N+1):
        case = get_Cases(content,i)
        results = "Case #"+str(i)+" "+sover(content,i)+"\n"
        a_out.write(results)
content = read_in("FreeCellStats_Small.in")
test = get_Cases(content,1)
