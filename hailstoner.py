import time

def step(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3*x + 1

def go(x):
    while True:
        print x
        x = step(x)
        time.sleep(1)

if __name__ == '__main__':
    try:
        print 'Welcome to Hailstoner! Enter any natural number to generate its hailstone sequence. Hit CTRL+D to exit.\n'
        while True:
            s = raw_input('seed: ')
            go(int(s))
    except EOFError:
        print 'Goodbye!'
