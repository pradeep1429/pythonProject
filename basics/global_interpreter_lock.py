import time
import threading

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

#GBL
start = time.time()
countdown(COUNT)
end = time.time()

print('With GBL time taken in seconds -', end - start)



COUNT = 50000000
# We split the work among two threads
t1 = threading.Thread(target=countdown, args=(COUNT//2,))
t2 = threading.Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('With threading time taken in seconds -', end - start)