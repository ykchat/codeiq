#(2) python 2.7

def sequence(num):

    for i in range(num):
        digits = format(i+1, 'b');
        term = 0
        for digit in digits:
            term *= 3
            term += int(digit)
        print term

if __name__ == '__main__':
    sequence(100)
