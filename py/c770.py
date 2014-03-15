# coding: UTF-8

def search(num):

    # 行の反転
    cols = [(2**num-1)*((2**num)**i) for i in range(num)]
    # 列の反転
    rows = [(((2**num)**num-1)/(2**num-1))*(2**i) for i in range(num)]

    # 塗り分けの組み合わせ生成
    combs = {i: False for i in range(2**(num**2))}

    # マス目の組み合わせ生成
    grids = [[i,j] for i in range(num) for j in range(num)]

    # すべて白からスタート
    curs = [0]
    combs[0] = True

    max = 0
    while True:
        nexts = []
        for cur in curs:
            for grid in grids:
                # 選択したマス目の行と列の色を反転
                next =((cur^cols[grid[0]])^rows[grid[1]])^(2**(num*grid[0]+grid[1]))
                # 出現済の場合、スキップ
                if combs[next]:
                    continue
                nexts.append(next)
                combs[next] = True
        # 出現未済がない場合、終了
        if len(nexts) == 0:
            break
        curs = nexts
        max += 1

    # 最後まで残ったものが答え
    print [format(cur, 'b').zfill(16) for cur in curs], max

if __name__ == '__main__':

    num = 4

    search(num)
