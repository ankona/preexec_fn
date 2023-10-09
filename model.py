import os
import subprocess
import sys
import time


def main():
    print('in main of model, current pid is:', os.getpid())
    print('in main of model, sys.argv is:', sys.argv)

    time.sleep(1)

    print('leaving main of model')

if __name__ == "__main__":
    main()
    sys.exit(0)
