import random

def get_lucky_nums():
    result = random.sample(range(1,46), k=6)

if __name__ == '__main__':
    times = int(input('Enter num(1-100): '))
    for _ in range(times):
        print(get_lucky_nums())
