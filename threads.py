#coding utf-8

import threading
import time
import random

class MonThread(threading.Thread):
    def __init__(self, limit, name, delay):
        threading.Thread.__init__(self)
        self.limit = limit
        self.name = name
        self.delay = delay
        print(f'Tread {self.name} attendra {self.delay}s entre chaque exécution')

    def run(self):
        for i in range(self.limit):
            print(f'thread {self.name} : {i}')
            time.sleep(self.delay)


class MesThreads():
    def __init__(self):
        print('début')
        threads = list()

        interval = 3
        listeComplète = list()
        [listeComplète.append(chr(65+x)) for x in range(26)]
        listeRéduite = [listeComplète[i:i+interval] \
            for i in range(len(listeComplète)) if i%interval == 0]

        for listeThreads in listeRéduite:
            for unThread in listeThreads:
                threads.append(MonThread(3, unThread, random.randint(1, 10)/10))

            for unThread in threads:
                unThread.start()

            for unThread in threads:
                unThread.join()
            
            threads.clear()

        print('fin')

if __name__ == "__main__":
    MesThreads()
