# coding: UTF-8

def search(num):

    # 組み合わせ生成
    combs = {'': None}
    for i in range(num):
        tmps = {}
        for j in range(6):
            for comb in combs:
                tmps[comb+str(j+1)] = None
        combs = tmps

    # ループするかしないかの選別
    for rolls in combs:
        # 選別済の場合、スキップ
        if combs[rolls] is not None:
            continue
        steps = []
        loop = 0
        while True:
            steps.append(rolls)
            roll = int(rolls[0])
            next = rolls[roll:] 
            next += str(int('7'*roll)-int(rolls[:roll]))
            # 選別済の目の場合、終了
            if combs[next] is not None:
                loop = len(steps)
                break
            # ループした場合、終了
            if next in steps:
                loop = steps.index(next)
                break
            rolls = next
        for rolls in steps[:loop]:
            combs[rolls] = 1
        for rolls in steps[loop:]:
            combs[rolls] = 0

    print sum(combs.values())

if __name__ == '__main__':
    search(6)
