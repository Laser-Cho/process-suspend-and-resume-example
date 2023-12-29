import psutil
import sys

def pause_resume_process(pid):
    process = psutil.Process(pid)
    if process.status() != psutil.STATUS_STOPPED:
        process.suspend()
        print("Process Paused")
    else:
        process.resume()
        print("Process Resumed")


if __name__ == "__main__":
    pid = int(sys.argv[1])
    if "-k" in sys.argv:
        process = psutil.Process(pid)
        process.kill()
    else:
        pause_resume_process(pid)