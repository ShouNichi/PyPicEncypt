import numpy as np
from PIL import Image


# Image to array
data = np.array((Image.open('encrypted')))
cache = np.zeros(data.shape, dtype=data.dtype)

# height, width, a number used to generate new numbers, password
h = data.shape[0]
w = data.shape[1]
global_passwd = 0.123456  # Real password
passwd = global_passwd
u = 3.9999999

# Calculate password for column decryption
for x in range(h):
    chaos = [passwd]
    for p in range(1, w):  # 每行5个,生成混沌序列
        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
    passwd = chaos.pop()
    del chaos

    
for x in range(w):  # Column
    chaos = [passwd]
    mapping = {}
    address = {}

    for p in range(1, h):
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

    
passwd = global_passwd
for x in range(h):  # Row
    chaos = [passwd]
    mapping = {}
    address = {}

    for p in range(1, w):
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
    
# Array to image
test = Image.fromarray(data)
test.save('decrypted.png')
