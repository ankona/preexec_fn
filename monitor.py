import os
import psutil
import subprocess
import sys
import argparse


def monitor(pid: int) -> None:
    print("in monitor.start_monitor (preexec_fn), target pid is:", pid)
    print('in monitor.start_monitor (preexec_fn), sys.argv is:')

    result = None
    try:
        proc = psutil.Process(pid)
        result = proc.wait()
        with open('monitor.out', 'w+') as monitor_fp:
            monitor_fp.write(f"monitored process retval is: {result}")
    except Exception as ex:
        print(ex)
        with open('monitor.out', 'w+') as monitor_fp:
            monitor_fp.write(f"{ex}")

    print(f'monitoring of model process {pid} is complete. model returned: {result}')


if __name__ == "__main__":
    monitor_pid = os.getpid()

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=None, type=int)

    args = sys.argv[1:]
    # args = sys.argv
    print('in monitor.py __main__(pid=', monitor_pid, '}), sys.argv:', args)
    ns = parser.parse_args(args)
    pid2monitor = ns.p
    # pid2monitor = int(os.environ["PID"])
    
    monitor(pid2monitor)
