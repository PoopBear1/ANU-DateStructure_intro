from Stack import*
from CircularQueue import*
from BoundedQueue import*
from time import*


def Stackruntime():

    stack = Stack(80000)
    for i in range(stack.capacity()):
        stack.push(i)
    start = time()
    for i in range(40000):
        try:    
            stack.pop()
        except:
            raise Exception('Error: Stack is empty')
    
    end = time()
    time_interval = end - start
    return time_interval

def Bqueruntime():

    q=BoundedQueue(80000)
    for i in range(q.capacity()):
        q.enqueue(i)
    start = time()
    for i in range(40000):
        try:    
            q.dequeue()
        except:
            raise Exception('Error: Queue is empty')
    end = time()
    time_interval = end - start
    return time_interval
        

def Cqueruntime():

    p=CircularQueue(80000)
    for i in range(p.capacity()):
        p.enqueue(i)
    start=time()
    for i in range(40000):
        try:
            p.dequeue() 
        except:
            raise Exception('Error: Queue is empty')
    end = time()
    time_interval= end-start
    return time_interval
   
if __name__ == '__main__':
    print('Runtime for Stack: '+str(Stackruntime())+'s')
    print('Runtime for BoundedQueue: ' +str(Bqueruntime())+'s')
    print('Runtime for CircularQueue: '+str(Cqueruntime())+'s')
    # print('Difference: '+str(runtime2()-runtime1())+'s')
    
