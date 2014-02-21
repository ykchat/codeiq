# coding: UTF-8

def search(num):

    routes = []

    for i in range(4**num):
        route = format(i, 'b')
        if route.count('1') == num:
            routes += [route.zfill(2*num)]

    oks = 0

    for mroute in routes:
        for wroute in routes:
            mpos = [0, 0]
            wpos = [num, num]
            passed = False
            for mmov, wmov in zip(mroute, wroute): 
                mpos[int(mmov)] += 1
                wpos[int(wmov)] -= 1
                if mpos == wpos:
                    oks += 1
                    break
                elif mpos[0] == wpos[0] or mpos[1] == wpos[1]:
                    if passed:
                        oks += 1
                        break
                    else:
                        passed = True

    print oks

if __name__ == '__main__':
    search(6)
