import textwrap

def wrap(string, max_width):
    s=textwrap.fill(string,max_width) #wrap with the lengthand print in separate lines
    w=textwrap.wrap(string,max_width) #wrap and print in a list
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)