import numpy as np
from PIL import Image
from tqdm import trange

def picDecrypt(file,password):
	# Image to array
	data = np.array(file)
	cache = np.zeros(data.shape, dtype=data.dtype)
	
	# height, width, a number used to generate new numbers, password
	h = data.shape[0]
	w = data.shape[1]
	global_passwd = password # Real password
	passwd = global_passwd
	u = 3.9999999
	
	# Calculate password for column decryption
	print('\nCalculating Password...')
	for x in trange(h):
	    chaos = [passwd]
	    for p in range(1, w+1):
	        chaos.append(u * chaos[p - 1] * (1 - chaos[p - 1]))
	    passwd = chaos.pop()
	    del chaos
	
	print('\nDecryping Column...')
	for x in trange(w):  # Column
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
	        cache[address[d]][x] = data[d][x]
	    del address
	
	print('\nDecrypting Rows...')
	passwd = global_passwd
	for x in trange(h):  # Row
	    chaos = [passwd]
	    mapping = {}
	    address = {}
	
	    for p in range(1, w+1):
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
	result = Image.fromarray(data)
	return result
	
if __name__ == '__main__':
	import time
	image = Image.open(input('Path：'))
	pword = float(input('Password(0-1)：'))
	if not 0<pword<1:raise ValueError
	save_path = input('Save to：')
	start_time = time.time()
	picDecrypt(image,pword).save(save_path)
	input('\nDecryption Finished...\nTime: {:.6f} second(s)\nPress any key...'.format(time.time()-start_time))
	