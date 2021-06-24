from random import randint
from time import sleep
import sys, os

HEIGHT = 24
WIDTH = 80
PAUSE_DURATION = 0.15
NUMBER_OF_POINTS = 250
EXPLOSION_DURATION = randint(1, 10)
MIN_EXPLOSION_FREQUENCY = 10
MAX_EXPLOSION_FREQUENCY = 50

UNLIT = '.'
LIT = chr(9604)

def main():
    fuses = []
    for i in range(NUMBER_OF_POINTS):
        fuse = {}
        fuse['timeForExplosion'] = randint(MIN_EXPLOSION_FREQUENCY, MAX_EXPLOSION_FREQUENCY)
        fuse['exploding'] = False
        fuses.append(fuse)

    while True:
        litFuse = []
        unlitFuse = []

        for fuse in fuses:
            point = (randint(0, 80), randint(0, 24))

            fuse['timeForExplosion'] -= 1
            if fuse['timeForExplosion'] <= 0:
                if fuse['exploding']:
                    fuse['timeForExplosion'] = randint(MIN_EXPLOSION_FREQUENCY, MAX_EXPLOSION_FREQUENCY)
                else:
                    fuse['timeForExplosion'] = EXPLOSION_DURATION
                fuse['exploding'] = not fuse['exploding']

            if fuse['exploding']:
                litFuse.append(point)
            else:
                unlitFuse.append(point)

            showExplosions(litFuse, unlitFuse)
            sleep(PAUSE_DURATION)
            clearScreen()

def showExplosions(litFuse, unlitFuse):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in litFuse:
                print(LIT, end='')
            elif (x, y) in unlitFuse:
                print(UNLIT, end='')
            else:
                print(' ', end='')
        print()

def clearScreen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()