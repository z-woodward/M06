#ZacharyW - 15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.

import multiprocessing as mp
from datetime import datetime
import time
import random

def process():
    stalling = random.random()
    time.sleep(stalling)
    print(datetime.now())

if __name__ == '__main__':
    for number in range(3):
        datetime = mp.Process(target=process)
        datetime.start()