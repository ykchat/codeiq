# coding: UTF-8

def search(num):

    # マスク
    rmask = sum([1<<i for i in range(num)])
    cmask = sum([1<<(num*i) for i in range(num)])
    masks = [(rmask<<(row*num))|(cmask<<col) for row in range(num) for col in range(num)]

    # 塗り分けの組み合わせ生成
    combs = {i: -1 for i in range(2**(num**2))}

    # すべて白からスタート
    curs = [0]
    combs[0] = 0

    max = 0
    while True:
        nexts = []
        for cur in curs:
            for mask in masks:
                # 選択したマス目の行と列の色を反転
                next = cur ^ mask
                # 出現済の場合、スキップ
                if combs[next] != -1:
                    continue
                nexts.append(next)
                combs[next] = max + 1
        # 出現未済がない場合、終了
        if len(nexts) == 0:
            break
        curs = nexts
        max += 1

    # 最後まで残ったものが答え
    for cur in curs:
        print "初期状態:%s, 最大ステップ数:%d" % (format(cur, 'b').zfill(16), max)

if __name__ == '__main__':

    num = 4

    search(num)

