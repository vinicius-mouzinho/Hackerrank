def print_formatted(number):
    w = len(bin(number)[2:])

    for i in range(1, number + 1):
        o = str(oct(i)[2:])
        h = str(hex(i)[2:].upper())
        b = str(bin(i)[2:])

        print(str(i).rjust(w), end=' ')
        print(str(o).rjust(w), end=' ')
        print(str(h).rjust(w), end=' ')
        print(str(b).rjust(w))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)