import undetected_chromedriver.v2 as uc
from worker import Worker
import threading
 
class thread(threading.Thread):
    def __init__(self, thread_data, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_data
        self.thread_ID = thread_ID
        self.worker = Worker()

    def run(self):
        print(str(self.thread_name) +" "+ str(self.thread_ID))
        self.worker.main_runner()


# thread1 = thread("thread1", 1000)
thread2 = thread("thread2", 2000);

# thread1.start()
thread2.start()
