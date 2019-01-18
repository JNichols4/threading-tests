import threading
from threading import Thread
import numpy as np
import time
import Queue


def process_number(number,out_queue):
    number_ref = number
    step_count = 0
    if number_ref==0:
        out_queue.put(step_count)
    if number_ref==1:
        out_queue.put(step_count+1)
    while True:
        if number_ref==1:
            break
        elif (number_ref%2)==0:
            number_ref = number_ref / 2
            step_count+=1
        elif (number_ref%2)==1:
            number_ref = (number_ref * 3) + 1
            step_count += 1
    out_queue.put(step_count)

#ulam's problem using threaded processes
number_array = np.arange(1,1000000,1)
number_array = np.float64(number_array)

processor_threads = 4

my_queue = Queue.Queue()

print("processing 15...")
process_number(15, my_queue)
print("Steps taken: {}".format(my_queue.get()))

threads = []
for i in range(processor_threads):
    number = number_array[i]
    threads.append(Thread(target=process_number,name='Worker_{}'.format(i),args=(number,my_queue)))

print threads

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print list(my_queue.queue)