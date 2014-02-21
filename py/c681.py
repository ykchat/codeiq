symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def main(roman):

    arabic = 0

    prev = 0

    for symbol in roman[::-1]:
        value = symbols[symbol]
        if value < prev:
            arabic -= value
        else:
            arabic += value
        prev = value

    print "%s = %d" % (roman, arabic)

if __name__ == '__main__':
    main('XLIX')
    main('MDCCCLXXXVIII')
    main('MCMXLV')
    main('MMMCMXCIX')
