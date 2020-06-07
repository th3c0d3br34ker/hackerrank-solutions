if __name__ == '__main__':
    N = int(raw_input())
    l=[]
    for i in range(N):
        inp = raw_input().strip().split()
        command = inp[0]
        values = inp[1:]
        if command == 'print':
            print(l)
        else:
            execute = 'l.' + command + "(" + ",".join(values) + ")"
            eval(execute)


