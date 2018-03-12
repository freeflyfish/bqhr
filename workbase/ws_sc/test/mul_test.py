from multiprocessing import Process,Lock,RLock
import time
import os


def foo1(lock):
    lock.acquire()
    # time.sleep(1)
    # print('hello--'+str(name))
    # print(os.getppid(), '-----------', os.getpid())
    for x in range(3):
        if x == 1:
            lock.release()
            # time.sleep(3)
        print(x)


class foo3(object):
    def __init__(self, *args):
        print(args)


def foo2(lock):
    lock.acquire()
    # time.sleep(1)
    # print('login--'+str(name))
    # print(os.getppid(), '-----------', os.getpid())
    for x in range(5):
        print('login')
    lock.release()
process_list = []
lock = RLock()
if __name__ == '__main__':
    dic = {
        'foo1': foo1,
        'foo2': foo2,
        'foo3': foo3
    }
    for foo in dic.values():
        p = Process(target=foo, args=(lock,))
        p.start()
        process_list.append(p)
    for j in process_list:
        j.join()