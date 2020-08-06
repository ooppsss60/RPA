import os
import time
import logging

from listener import Listener, worker

if __name__ == '__main__':
    logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
    os.makedirs('screenshots', exist_ok=True)
    listener = Listener()
    listener.start()
    time.sleep(5)
    listener.stop()
    worker.stop()
