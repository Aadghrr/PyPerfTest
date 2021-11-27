import dis, os

TEST_ARRAY = list(range(100000))

def testComprehension():
    return [i*i for i in TEST_ARRY]

def testLoop():
    a=[]
    for i in TEST_ARRAY:
        a.append(i*i)
    return a

dis.dis(testLoop)

dis.dis(testComprehension)

if __name__=='__main__':
    print(os.getpid())
    while True:
        testLoop()
