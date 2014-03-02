# coding: UTF-8

import re

def search(nums):

    # 2個表示の組合せ
    combs2 = {}
    for i in range(10):
        for j in range(10):
            if i == j:
                continue
            combs2[str(i)+str(j)] = format(nums[i]^nums[j], 'b').count('1')

    # 3個表示の組合せ
    combs3 = {}
    for comb, nsw in combs2.items():
        for i in range(10):
            if str(i) in comb:
                continue
            combs3[comb+str(i)] = nsw + format(nums[int(comb[1])]^nums[i], 'b').count('1')

    # 5個表示の組合せ
    combs5 = {}
    minnsw5 = None
    for comb1, nsw1 in combs3.items():
        for comb2, nsw2 in combs2.items():
            if re.search('['+comb2+']', comb1) is not None:
                continue
            combs5[comb1+comb2] = nsw1 + format(nums[int(comb1[2])]^nums[int(comb2[0])], 'b').count('1') + nsw2

    mincomb10 = None
    minnsw10 = max(combs5.values())*2 + max(combs2.values())
    minnsw5 = min(combs5.values())
    minnsw2 = min(combs5.values())

    # 10個表示の組合せ
    for comb1, nsw1 in sorted(combs5.items(), key=lambda x:x[1]):
        # 最小切替回数が現れる可能性がなくなったらループ終了
        if minnsw10 <= (nsw1 + minnsw2 + minnsw5):
            break
        for comb2, nsw2 in sorted(combs5.items(), key=lambda x:x[1]):
            if re.search('['+comb2+']', comb1) is not None:
                continue
            nsw = nsw1 + format(nums[int(comb1[4])]^nums[int(comb2[0])], 'b').count('1') + nsw2
            if minnsw10 > nsw:
                mincomb10 = comb1+comb2
                minnsw10 = nsw
            # 最小切替回数が現れる可能性がなくなったらループ終了
            else:
                break

    print "最小切替回数:%d, 表示順:%s" % (minnsw10, mincomb10)

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
