import numpy as np
from PIL import Image

def readimage(path):
	return Image.open(path)


def image_proc(file, passwd, proctype):
    data = np.array(file)
    cache = np.zeros(data.shape, dtype=data.dtype)
    h = data.shape[0]
    w = data.shape[1]

    u = 3.9999999
    big = max(w, h)
    small = min(w, h)
    chaos = [0]
    chaos[0] = float(passwd)
    mappingmax = {}
    mappingmin = {}
    xmapping = {}
    ymapping = {}

    for p in range(1, big):
        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))

    chaosmin = [0]
    chaosmin[0] = chaos[-1]

    for p in range(1, small):
        chaosmin.append(u * chaosmin[p - 1] * (1 - chaosmin[p - 1]))

    p = 0
    for x in chaos:
        mappingmax[x] = p
        p += 1

    p = 0
    for x in chaosmin:
        mappingmin[x] = p
        p += 1

    chaos.sort()
    chaosmin.sort()

    if w >= h:
        p = 0
        for x in chaos:
            xmapping[mappingmax[x]] = p
            p += 1

        p = 0
        for x in chaosmin:
            ymapping[mappingmin[x]] = p
            p += 1
    else:
        p = 0
        for x in chaos:
            ymapping[mappingmax[x]] = p
            p += 1

        p = 0
        for x in chaosmin:
            xmapping[mappingmin[x]] = p
            p += 1
    if proctype == 'e':

        for x in range(h):
            for p in xmapping.keys():
                cache[x][p] = data[x][xmapping[p]]

        for p in ymapping.keys():
            data[p] = cache[ymapping[p]]
    else:
        for p in ymapping.keys():
            cache[ymapping[p]] = data[p]

        for x in range(h):
            for p in xmapping.keys():
                data[x][xmapping[p]] = cache[x][p]

    final_image = Image.fromarray(data)
    return final_image


if __name__ == '__main__':
    a = input('输入文件：')
    b = input('输入小数（0-1）：')
    c = input('处理方式:')
    fin = image_proc(a, b, c)
    d = input('输入保存文件名')
    fin.save(d)
    input('完成，按任意键继续...')
