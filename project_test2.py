import time
import threading 
import random

wID = 1 # initialize westbound car's ID
eID = 1 # initialize eastbound car's ID

def w_Job():
    while(True):
        global wID
        car = Car('w', wID)
        car.start()
        next_car = random.uniform(3,5)  # new car created time / float random (3,5)
        time.sleep(next_car)
        wID += 1

def e_Job():
    while(True):
        global eID
        car = Car('e', eID)
        car.start()
        next_car = random.uniform(3,5)
        time.sleep(next_car)
        eID += 1


class Bridge():

    sem = threading.Semaphore(3)
    cond = threading.Condition()
    event = threading.Event()
    waiting = False
    CarOnBridge = 0
    
    
    def __init__(self):
        pass

    def crossBridge(self, Car):
        Bridge.sem.acquire()
        print(Car.name + ' is WAITING to cross the bridge.')

        if(Bridge.waiting == False):
            Bridge.cond.acquire()
            
        if(Bridge.CarOnBridge == 0 or Car.name[0] == Bridge.dir):
             
            Bridge.dir = Car.name[0]
            Bridge.CarOnBridge += 1
            print(Bridge.dir , Bridge.CarOnBridge , 'if1')
            Bridge.cond.release()
            print(Car.name + ' is CROSSING the bridge!!!!!!!!')
            periods = random.uniform(1,3)  
            time.sleep(periods)  # the periods of crossing the bridge            
            print(Car.name + ' has LEFT the bridge......')
     
            Bridge.CarOnBridge -= 1
         
            if(Bridge.CarOnBridge == 0 and Bridge.waiting == True):
#                Bridge.cond.acquire()
                print(Car.name +  ' notify1 ')
                Bridge.event.set()
#                Bridge.cond.notify()
#                Bridge.cond.release()
                Bridge.waiting = False
        else:
            Bridge.waiting = True
            print(Car.name + ' is wait wait wait.')
            Bridge.event.wait()
            print(Car.name + ' finished waiting')
            Bridge.event.clear()
            Bridge.dir = Car.name[0]
            
            Bridge.CarOnBridge += 1
            print(Bridge.dir , Bridge.CarOnBridge , "if2")

            Bridge.cond.release()

            print(Car.name + ' is CROSSING the bridge!')
            periods = random.uniform(1,3)  
            time.sleep(periods)  # the periods of crossing the bridge            
            print(Car.name + ' has LEFT the bridge.')

            Bridge.CarOnBridge -= 1
   
            if(Bridge.CarOnBridge == 0 and Bridge.waiting == True):
#                Bridge.cond.acquire()
                print(Car.name + ' notify2')
                Bridge.event.set()
#                Bridge.cond.notify()
#                Bridge.cond.release()
                Bridge.waiting = False

       
        Bridge.sem.release()
        
        
        

class Car(threading.Thread):
    
    def __init__(self, name, num):
        threading.Thread.__init__(self)
        self.name = name
        self.num = num
#    def getName(self):
#        return self.name

#    def setName(self):
#        self.name

    def run(self):
        if self.name == 'w':
            self.name = ('Westbound car' + str(self.num))
            print(self.name)
            Bridge.crossBridge(Bridge,self)
        else:
            self.name = ('Eastbound car' + str(self.num)) 
            print(self.name)
            Bridge.crossBridge(Bridge, self)

def main():
    Western = threading.Thread(target= w_Job)
    Eastern = threading.Thread(target= e_Job)
    Western.start()
    Eastern.start()

if __name__=="__main__":
    main()