# coding: UTF-8
# Note: 0を必ず含む場合に変更

def search(num):

    terms = [0] * num

    i = 0
    while 0 in terms:
        i += 1
        digits = format(i, 'b')
        if not '0' in digits:
            continue
        value = 0
        for digit in digits:
            value *= 10
            value += int(digit) * 7
        for j in range(num):
            if terms[j] != 0:
                continue
            if value % (j+1) == 0:
                terms[j] = value

    i = 0
    for term in terms:
        i += 1
        digits = str(term)
        if digits == digits[::-1]:
            print "n = %d のとき　%d * %d = %d" % (i, i, term/i, term)

if __name__ == '__main__':
    search(50)
