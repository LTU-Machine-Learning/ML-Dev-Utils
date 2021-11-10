import sys
import signal
import time


def exit_gracefully(signum, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)


def long_taks():
    sleep_seconds = 5
    for i in range(60, 0, -1):
        now = time.localtime()
        now = time.strftime("%H:%M:%S", now)
        print(f"Now it's {now}. "
              f"I will sleep for {sleep_seconds} seconds for {i} times.")
        time.sleep(sleep_seconds)


if __name__ == "__main__":
    """
    Use src/check/run_detached.sh|stop_detached.sh to try out
    """
    print("Hello Background Run!")
    print(f"Running Python {sys.version_info}")
    print("Stop with CTRL+C")
    try:
        long_taks()
    except SystemExit as ex:
        print("Killing me softly (SystemExit)")
    except Exception as ex:
        print('Exception occured!', exc_info=ex)
    finally:
        print("run closed")
