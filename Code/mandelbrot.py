import time
import multiprocessing
import matplotlib.pyplot as plt
from functools import partial

# pool_size = 1 # the number of processes in the poll - this can be changed later. 

def mandelbrotCalcSet(poolsize, h, w, max_iteration = 1000):
    tp1 = time.time()
    #make a helper function that better supports pool.map by using only 1 var
    partialCalcRow = partial(mandelbrotCalcRow, h=h, w=w, max_iteration = max_iteration)
 
    pool = multiprocessing.Pool(processes=poolsize) #creates a pool of process, controls worksers
    #the pool.map only accepts one iterable, so use the partial function
    #so that we only need to deal with one variable.
    mandelImg = pool.map(partialCalcRow, range(h)) # Build the image a row at a time.
    
    pool.close() #we are not adding any more processes
    pool.join() #tell it to wait until all threads are done before going on
    total_time = time.time()-tp1
    print("Overall Time:", total_time)
    return mandelImg, total_time

def mandelbrotCalcRow(yPos, h, w, max_iteration = 1000):
    y0 = yPos * (2/float(h)) - 1 #rescale to -1 to 1
    row = []
    for xPos in range(w):
        x0 = xPos * (3.5/float(w)) - 2.5 #rescale to -2.5 to 1
        iteration, z = 0, 0 + 0j
        c = complex(x0, y0)
        while abs(z) < 2 and iteration < max_iteration:
            z = z**2 + c
            iteration += 1
        row.append(iteration)
 
    return row


#runtimes = [];
#
#pool_size = 1
#if __name__ == '__main__':
#	print("Running on 1 processor...")
#	mandelImg, rt = mandelbrotCalcSet(pool_size, 500, 500, 1000)
#	runtimes.append(rt)
#	plt.imshow(mandelImg)
#	plt.savefig("mandelimg1.png")
#	
#pool_size = 2
#
#if __name__ == '__main__':
#	print("Running on 2 processors...")
#	mandelImg, rt = mandelbrotCalcSet(pool_size, 500, 500, 1000)
#	runtimes.append(rt)
#	plt.imshow(mandelImg)
#	plt.savefig("mandelimg2.png")
#
#pool_size = 4
#
#if __name__ == '__main__':
#	print("Running on 4 processors...")
#	mandelImg, rt = mandelbrotCalcSet(pool_size, 500, 500, 1000)
#	runtimes.append(rt)
#	plt.imshow(mandelImg)
#	plt.savefig("mandelimg4.png")
#	
#pool_size = 8
#
#if __name__ == '__main__':
#	print("Running on 8 processors...")
#	mandelImg, rt = mandelbrotCalcSet(pool_size, 500, 500, 1000)
#	runtimes.append(rt)
#	plt.imshow(mandelImg)
#	plt.savefig("mandelimg8.png")
#	
#print(runtimes)
