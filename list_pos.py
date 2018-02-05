from glob import glob

import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="positive")
parser.add_argument("-o", "--output", type=str, default="positive.dat")
parser.add_argument("-w", "--width", type=int)
parser.add_argument("--height", type=int)
parser.add_argument("-e", "--extension", type=str, default="jpg")
parser.add_argument("-n", "--number", type=int)
args = parser.parse_args()

print ('Trying to list {} files...'.format(args.number))

positives = glob("%s/*.%s" % (args.input, args.extension))[:args.number]

def trans(filename):
    unescape = filename.replace(os.sep, '/')
    return "%s 1 0 0 %d %d" % (unescape, args.width, args.height)

positives = map(trans, positives)

print("Listed {} files".format(len(list(positives))))
print(" Output file = {}".format(args.output))

with open(args.output, "w") as out_file:
    for item in positives:
        out_file.write("%s\n" % item)
        print("item = {}".format(item))
