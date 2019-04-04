import cv2
import os
import sys
import time

## split 01.mpg -o frames/ -d

DEBUG = False

def split(vid, output):
    if DEBUG:
        print('Splitting: ', vid)
        print('Output dir:', output)
        start = time.time()

    cap = cv2.VideoCapture(vid)
    success, img = cap.read()
    count = 0
    while success:
        if DEBUG:
            print('Writing {}{}_frame{}.jpg...'.format(output, vid, count))
        cv2.imwrite('{}{}_frame{}.jpg'.format(output, vid, count), img)
        success, img = cap.read()
        count += 1

    if DEBUG:
        end = time.time()
        print('Elapsed:', end - start)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments')
        exit(0)

    if sys.argv[1] == '-h':
        print('Usage: python split.py <videofile> [ -o <outputdir> ] [ -d ]')
        exit(0)

    vid = sys.argv[1]
    
    if len(sys.argv) > 2 and sys.argv[2] == '-o':
        output = sys.argv[3]
    else:
        output = ''

    if '-d' in sys.argv:
        DEBUG = True

    split(vid, output)
