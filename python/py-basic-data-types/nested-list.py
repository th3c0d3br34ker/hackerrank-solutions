if __name__ == '__main__':
    students=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        t=[]
        t.append(name)
        t.append(score)
        students.append(t)

    students.sort( key = lambda x: x[1])
    min_score=students[0][1]
    flag=True

    while(flag):
        students=students[1:]
        if(students[0][1]!=min_score):
            flag=False

    min_score=students[0][1]
    l=[]
    for i in students:
        if(i[1]==min_score):
            l.append(i[0])
    
    l.sort()
    for i in l:
        print(i)

