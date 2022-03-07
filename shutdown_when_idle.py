
def main():
    import psutil
    import time
    import argparse

    threshold = 1
    pause = 10
    wait = 1

    parser = argparse.ArgumentParser(description="Turns off the computer when the cpu usage is below a given threshold")
    parser.add_argument(
        "-t",
        required=False,
        type=float,
        default=threshold,
        help=f"the cpu usage percentage under which the computer will be turned off, defaults to {threshold}%."
        )
    parser.add_argument(
        "-p", 
        required=False,
        type=int,
        default=pause,
        help=f"the script checks to see if the cpu usage is below the threshod at this interval, defaults to {pause}."
        )
    parser.add_argument(
        "-w",
        required=False,
        type=int,
        default=wait,
        help=f"the number of minutes ahead to schedule the shutdown when the computer starts to idle. The shutdown can be aborted during this period. Defaults to {wait}."
        )
    args = vars(parser.parse_args())
    threshold = args["t"]
    pause = args["p"]

    print(f"Will automatically shut down the computer when the cpu usage is below {threshold}%")
    print(f"Checking every {pause} seconds")
    psutil.cpu_percent()
    while True:
        time.sleep(pause)
        usage = psutil.cpu_percent()
        if usage < threshold:
            print("CPU usage is below threshold, initializing shutdown...")
            abortable_shutdown(wait)

def abortable_shutdown(wait = 1):
    """Schedules a shutdown <wait> minutes in the future. Allows the user to abort the shutdown by pressing enter."""
    import subprocess
    import sys

    if sys.platform == "win32":
        subprocess.run(["shutdown","/s",f"/t {wait*60}"])
        input("Press enter to abort shutdown")
        subprocess.run(["shutdown","/a"])
    else:
        subprocess.run(["shutdown",f"{wait}"])
        input("Press enter to abort shutdown")
        subprocess.run(["shutdown","-c"])

    exit()

if __name__ == '__main__':
    main()

