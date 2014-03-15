# coding: UTF-8

def search(num):

    combs = {}

    # 組合せ生成
    gen(combs, '', num)

    # 並替え変化
    for comb in combs:
        change(combs, comb)

    print "並び:%s, 最大回数:%d" % max(combs.items(), key=lambda x:x[1])

def gen(combs, seq, size):

    if len(seq) == size:
        if seq[0] == '1':
            combs[seq] = 0
        else:
            combs[seq] = -1
        return

    for i in range(1, size+1):
        if seq.count(str(i)) == 1:
            continue
        nseq = seq + str(i)
        gen(combs, nseq, size)

def change(combs, comb):

    # 出現済の場合、既出の結果を返す
    if combs[comb] != -1:
        return combs[comb]

    i = int(comb[0])
    cnt = change(combs, comb[i-1::-1] + comb[i:]) + 1
    combs[comb] = cnt
    return cnt

if __name__ == '__main__':

    num = 9

    search(num)
