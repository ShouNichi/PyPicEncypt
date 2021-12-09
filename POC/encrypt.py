import numpy as np
from PIL import Image

# Image to array
data = np.array((Image.open('source.png')))
cache = np.zeros(data.shape, dtype=data.dtype)

# height, width, a number used to generate new numbers, password
h = data.shape[0]
w = data.shape[1]
u = 3.9999999
passwd = 0.123456  # password(0-1,float)


for x in range(h):  # row
	chaos = [passwd]
	mapping = {}
	address = {}
	
	for p in range(1,w+1):  # generate chaotic sequence
		chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
	passwd = chaos.pop()  # Pop out the last one as the password for the next iteration

	p = 0
	for temp in chaos:  # Create an index
		mapping[temp] = p
		p += 1
		
	chaos.sort()
	
	p = 0
	for temp in chaos:  # Create an address map
		address[mapping[temp]] = p
		p += 1

	del chaos
	del mapping
	for d in address.keys():
		cache[x][d] = data[x][address[d]]
	del address

	
for x in range(w):  # column
	chaos = [passwd]
	mapping = {}
	address = {}

	for p in range(1, h+1):
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
		data[d][x] = cache[address[d]][x]
	del address

# Array to image
test = Image.fromarray(data)
test.save('encrypted.png')
