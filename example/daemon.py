import os
import time
import atexit
import signal

class createDaemon(object):
    def __init__(self, do_fork=True):
        """ 
            This function create a service/Daemon that will execute a det. task
        """

        self.msg = "Test msg %d"
        self.do_fork = do_fork
        try:
            # Store the Fork PID
            with open("/tmp/daemon.pids", "w") as f:
                self.pid = os.fork()
                f.write(f"{self.pid}|{os.getpid()}\n")

                if self.pid == 0:
                    print('PID: %d' % self.pid)
                    if not do_fork:
                        os._exit(0)
            
        except OSError as error:
            print('Unable to fork. Error: %d (%s)' % (error.errno, error.strerror))
            os._exit(1)

        self.doTask()

    def doTask(self):
        """ 
            This function create a task that will be a daemon
        """

        def signal_cb(s, f):
            os._exit(0)

        for s in signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT:
            signal.signal(s, signal_cb)

        # write pidfile
        def atexit_cb():
            print("Exit fork")

        atexit.register(atexit_cb)

        # Start the write
        i = 0
        while self.pid == 0 or not self.do_fork:
            print(self.msg % os.getpid())
            time.sleep(2)
            i += 1


if __name__ == '__main__':

    # Create the Daemon
    cdem = createDaemon(True)
    slave_pid = None
    time.sleep(1)
    with open("/tmp/daemon.pids", "r") as f:
        for l in f:
            pids_list = l.replace("\n", "").split("|")
            if pids_list[0] == "0":
                slave_pid = int(pids_list[1])

    for r in range(10):
        print("Main loop %d" % os.getpid())
        if r >= 5 and slave_pid:
            os.kill(slave_pid, signal.SIGQUIT)
        time.sleep(2)
