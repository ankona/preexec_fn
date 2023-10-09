import subprocess
import sys
import os
import multiprocessing
from monitor import monitor

def empty_fn() -> None:
    # print("in empty_fn (preexec_fn), current pid is:")
    # print('in empty_fn (preexec_fn), sys.argv is:')
    ...


def start_monitor() -> None:
    # print("in start_monitor (preexec_fn), current pid is:", os.getpid())
    # print('in start_monitor (preexec_fn), sys.argv is:')
    
    monitor = subprocess.Popen(
        [sys.executable, 
         "/Users/chris.mcbride/code/preexec_fn/monitor.py", 
         "-p", 
         str(os.getpid())],
        #  env={"PID": str(os.getpid())},
        #  stderr=subprocess.PIPE,
        #  stdout=subprocess.PIPE,
         close_fds=True,
    )
    monitor.poll()
    # monitor_result = monitor.poll()
    # print(f'in start_monitor, monitor_result is: {monitor_result}')


    # monitor_process = multiprocessing.Process(target=monitor, args=[os.getpid()], daemon=False)
    # monitor_process.start()


def main():
    print("in main, current pid is:", os.getpid())
    print('in main, sys.argv is:', sys.argv)

    proc = subprocess.Popen(
        [sys.executable, 
        "/Users/chris.mcbride/code/preexec_fn/model.py", "-a", "100"],
        preexec_fn=start_monitor,
        # preexec_fn=do_monitor,
        # stderr=subprocess.PIPE,
        # stdout=subprocess.PIPE,
        close_fds=True,
    )
    # proc.wait()
    result = proc.poll()
    while result is None:
        # print('looping...')
        result = proc.poll()
    print('in main, proc.poll() result:', result)


if __name__ == "__main__":
    main()
