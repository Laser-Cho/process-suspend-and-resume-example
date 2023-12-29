
import psutil
from tqdm import tqdm

def check_prime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True


def get_pid():
    current_pid = psutil.Process().pid
    print("PID :", current_pid)
    return current_pid

pid = get_pid()

for i in tqdm(range(100000000)):
    if check_prime(i) and (i-1)%33==0 :
        print(i, end=" ")

