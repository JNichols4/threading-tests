import multiprocessing as mp
from multiprocessing import Pool
import numpy as np
from multiprocessing import Queue

def collatz_iteration(number,output_queue):
    ex_num = number
    count = 0
    if ex_num == 0:
        output_queue.put(count)
        return count
    if ex_num == 1:
        output_queue.put(count+1)
        return count
    while ex_num!=1:
        if ex_num%2==0:
            ex_num = ex_num/2
            count +=1
        if ex_num%2==1:
            ex_num = (ex_num * 3) + 1
            count +=1
    output_queue.put(count)
    return count

pool = Pool(processes=4)
output_queue = Queue()
numbers = np.arange(1,100000,1)

pool.map(collatz_iteration,(numbers,output_queue))

print output_queue