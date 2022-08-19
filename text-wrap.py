import textwrap

def wrap(string, max_width):
    wrappedtext = textwrap.fill(string, max_width)
    return wrappedtext


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)