# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

import string
alphabets = string.ascii_lowercase


def print_rangoli(size):
    l = []
    for i in range(n):
        s = '-'.join(alphabets[i:n])
        l.append(s[::-1] + s[1:])
    for i in l[::-1]:
        print(i.center(4*n-3, '-'))
    for i in l[1:]:
        print(i.center(4*n-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
