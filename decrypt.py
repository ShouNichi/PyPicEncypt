import numpy as np
from PIL import Image
import time

start_time = time.time()

data = np.array((Image.open('加密结果.jpg')))
cache = np.zeros(data.shape, dtype=data.dtype)
h = data.shape[0]
w = data.shape[1]
passwd = 0.224356
u = 3.9999999
chaos = [passwd]

for x in range(h):
    chaos = [passwd]
    for p in range(1, w):  # 每行5个,生成混沌序列
        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
    passwd = chaos.pop()
    del chaos
print(time.time()-start_time)
for x in range(w):  # 列
    chaos = [passwd]
    mapping = {}
    address = {}

    for p in range(1, h):  # 每行5个,生成混沌序列
        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
    passwd = chaos.pop()

    p = 0
    for temp in chaos:
        mapping[temp] = p
        p += 1
    chaos.sort()
    p = 0
    for temp in chaos:
        address[mapping[temp]] = p
        p += 1

    del chaos
    del mapping
    for d in address.keys():
        cache[address[d]][x] = data[d][x]
    del address
print(time.time()-start_time)
passwd = 0.224356
for x in range(h):  # 行
    chaos = [passwd]
    mapping = {}
    address = {}

    for p in range(1, w):  # 每行5个,生成混沌序列
        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
    passwd = chaos.pop()

    p = 0
    for temp in chaos:
        mapping[temp] = p
        p += 1
    chaos.sort()
    p = 0
    for temp in chaos:
        address[mapping[temp]] = p
        p += 1

    del chaos
    del mapping
    for d in address.keys():
        data[x][address[d]] = cache[x][d]
    del address

test = Image.fromarray(data)
test.save('解密结果.png')

print(time.time()-start_time)