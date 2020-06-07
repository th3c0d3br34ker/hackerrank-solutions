def print_formatted(number):
    temp=str(bin(number))
    x=len(temp[2:])
    for i in range(1,number+1):
        dec=str(i)
        binary=str(bin(i))
        octal=str(oct(i))
        hexadec=str(hex(i))
        print("{0:>{x}} {1:>{x}} {2:>{x}} {3:>{x}}".format(dec,octal[2:],hexadec[2:].upper(),binary[2:],x=x))


