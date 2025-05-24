import multiprocessing
import subprocess

from engine.features import hotword

def start_jarvis():
    print('Process 1 is running')
    from main import start
    start()


def listen_hotword():
    print('Process 2 is running')
    hotword()
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=start_jarvis)
    p2 = multiprocessing.Process(target=listen_hotword)

    p1.start()
    subprocess.call([r'device.bat'])
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()
    print('system stop')



