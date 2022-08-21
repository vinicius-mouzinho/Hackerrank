# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
import re

def solve(s):
    names = s.split(' ')
    l = [i.capitalize() for i in names]
    return ' '.join(l)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
