from tqdm import tqdm
from time import sleep

# yield is used to create a generator object
# this function creates a generator object, which is a progress bar
# when this function is called, you can iterate each element generated
# the function tqdm will display a progress bar with the current progress
def ft_progress(lst):
    for i in tqdm(lst):
        yield i

def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    #print()
    #print(ret)

if __name__ == '__main__':
    main()