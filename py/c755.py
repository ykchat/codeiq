# coding: UTF-8

import re

def search(nums):

    size = len(nums)

    # 切替回数
    sw = [[format(nums[i]^nums[j], 'b').count('1') for i in range(size)] for j in range(size)]

    min = [7*(size-1), '']

    for i in range(size):
        trace(min, 0, str(i), size, sw)

    print "最小切替回数:%d, 表示順:%s" % tuple(min)

def trace(min, sum, seq, size, sw):

    if len(seq) == size:
        min[0] = sum
        min[1] = seq
        return

    for i in range(size):
        if seq.count(str(i)) == 1:
            continue
        nsum = sum + sw[int(seq[-1])][i]
        nseq = seq + str(i)
        if nsum < min[0]:
            trace(min, nsum, nseq, size, sw)

if __name__ == '__main__':

    nums = []
    nums.append(int('1111110', 2))
    nums.append(int('0110000', 2))
    nums.append(int('1101101', 2))
    nums.append(int('1111001', 2))
    nums.append(int('0110011', 2))
    nums.append(int('1011011', 2))
    nums.append(int('1011111', 2))
    nums.append(int('1110000', 2))
    nums.append(int('1111111', 2))
    nums.append(int('1111011', 2))

    search(nums)

