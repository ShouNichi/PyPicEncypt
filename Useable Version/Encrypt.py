import numpy as np
from PIL import Image
from tqdm import trange

def picEncrypt(file, password):
	# Image to array
	data = np.array(file)
	cache = np.zeros(data.shape, dtype=data.dtype)
	
	# height, width, a number used to generate new numbers, password
	h = data.shape[0]
	w = data.shape[1]
	u = 3.9999999
	passwd = password  # password(0-1,float)
	
	print('\n Encrypting Rows...')
	for x in trange(h):  # row
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
	
	print('\n Encrypting Columns...')
	for x in trange(w):  # column
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
	result = Image.fromarray(data)
	return result
	
if __name__ == '__main__':
	import time
	image = Image.open(input('Path：'))
	pword = float(input('Password(0-1)：'))
	if not 0<pword<1:raise ValueError
	save_path = input('Save to：')
	start_time = time.time()
	picEncrypt(image,pword).save(save_path,subsampling=0)
	input('\nEncryption Finished...\nTime:  {:.6f} second(s)\nPress any key...'.format(time.time()-start_time))
