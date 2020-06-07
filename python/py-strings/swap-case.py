def swap_case(s):
    t=""
    for i in s:
        if i.isalpha():
            if i.isupper():
                t=t+i.lower()
            else:
                t=t+i.upper()
        else:
            t=t+i

    return (t)


