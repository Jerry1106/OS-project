import threading 
import time

'''
def job():
    for i in range(5):
        print("Child thread: ", i)
        time.sleep(1)

t = threading.Thread(target = job) # target 為要讓t執行的函數

t.start() #執行t.start()的同時也會繼續下面的for工作


for i in range(3):
    print("Main thread: ", i)
    time.sleep(1) 

t.join()  # 等待t結束後才會執行下面的程序，
          # 由於Main只要3秒，為了等Child因此會在此停留2秒

print("Done.") 
'''
'''2
def job(num):    #根據num來決定要處理什麼工作  平行化程式
    print("Thread", num)
    time.sleep(1)

thread = []
for i in range(5):
    thread.append(threading.Thread(target = job, args = (i,))) # job(num)
    thread[i].start()
     
for i in range(5):
    thread[i].join()

print("Done.")
'''

'''
import time as tm
import threading as td
import queue as qe

class Worker(td.Thread):
    def __init__(self, qe, num):
        td.Thread.__init__(self)
        self.qe = qe
        self.num = num

    def run(self):
        while self.qe.qsize() > 0:
            msg = self.qe.get()
            print("Worker %d: %s" % (self.num, msg))
            tm.sleep(1)

my_queue = qe.Queue()
my_queue2 = qe.Queue()

for i in range(30):
    my_queue.put('Data: %d' %i)

for i in range(10):
    my_queue2.put('Data2: %d' %i)

my_workers1 = Worker(my_queue, 1)
my_workers2 = Worker(my_queue2, 2)

my_workers1.start()
my_workers2.start()

my_workers1.join()
my_workers2.join()

print("Done.")
'''


import time as tm
import threading as td
import queue as qe

class Worker(td.Thread):
    def __init__(self, qe, num, lock):
        td.Thread.__init__(self)
        self.qe = qe
        self.num = num
        self.lock = lock

    def run(self):
        while self.qe.qsize() > 0:
            msg = self.qe.get()
            
            self.lock.acquire()
            print('Lock acquired by Workers %d' % (self.num))

            print('Worker %d: %s' % (self.num, msg))
            tm.sleep(1)

            print('Lock released by Workers %d' % (self.num))
            lock.release()

my_queue = qe.Queue()
my_queue2 = qe.Queue()

lock = td.Lock()

for i in range(50):
    my_queue.put('Data: %d' %i)

for i in range(10):
    my_queue2.put('Data2: %d' %i)

            
my_workers1 = Worker(my_queue, 1, lock)
my_workers2 = Worker(my_queue, 2, lock)
#my_workers3 = Worker(my_queue, 3, lock)

my_workers1.start()
my_workers2.start()
#my_workers3.start()

my_workers1.join()
my_workers2.join()
#my_workers3.join()

print("Done.")