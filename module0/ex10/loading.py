from time import sleep
from time import time

# yield is used to create a generator object
# this function creates a generator object, which is a progress bar
# when this function is called, you can iterate each element generated
# the function tqdm will display a progress bar with the current progress
def ft_progress(lst):
    total = len(lst)
    progress = 0
    start = time()
    for elem in lst:
        yield elem
        progress += 1
        done = int(50 * progress / total)
        curr_time = int(time()-start)
        print(f"\r[{int(progress/total*100)}%][{'=' * done}{' ' * (50 - done)}]"
              f"{progress}/{total} {curr_time}s ETA: {int(curr_time/progress*total - curr_time)}s", end="")


def main():
    listy = range(3000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    #print()
    #print(ret)

if __name__ == '__main__':
    main()