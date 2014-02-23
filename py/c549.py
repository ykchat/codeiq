def generate_array_2d(modified, n, m):

    result = []

    if modified is False:
        for i in range(n):
            result.append([])
            for j in range(m):
                result[i].append(0)
    else:
        result =  [[0] * m for i in range(n)]

    return result

def flip_dict_items(modified, src):

    dst = {}

    if modified is False:
        for key in src:
            dst[src[key]] = key
    else:
        dst = {value:key for key, value in src.items()}

    return dst

if __name__ == '__main__':

    print("generate a 4 * 4 array")
    print(generate_array_2d(False, 4, 4))
    print(generate_array_2d(True, 4, 4))

    print("flip keys and values of a dictionary")
    print(flip_dict_items(False, {1: "a", 2: "b"}))
    print(flip_dict_items(True, {1: "a", 2: "b"}))
