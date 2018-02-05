# import pdb
# pdb.set_trace()

from PIL import Image
from glob import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="random")
parser.add_argument("-o", "--output", type=str, default="negative")
parser.add_argument("-w", "--width", type=int)
parser.add_argument("--height", type=int)
parser.add_argument("-e", "--extension", type=str, default="jpg")
parser.add_argument("-n", "--number", type=int)

args = parser.parse_args()

print("Trying to generate {} negative samples".format(args.number))

def main():
    src_imgs = glob(args.input + "/*.jpg")
    src_imgs.extend(glob(args.input + "/*.png"))

    count = 0
    w, h = args.width, args.height
    for src in src_imgs:
        if count > args.number:
            break
        im = Image.open(src).convert('1', dither=Image.NONE)
        W, H = im.size

        if W < w or H < h:
            im.save("%s/%d.%s" % (args.output, count, args.extension))
            count += 1
            continue

        for i in range(0, int(W/w)):
            if count > args.number:
                break
            for j in range(0, int(H/h)):
                if count > args.number:
                    break
                slice = im.crop((i * w, j * h, (i+1) * w, (j+1) * h))
                slice.save("%s/%d.%s" % (args.output, count, args.extension))
                count += 1

        if count % (args.number / 10) == 0:
            print("Finished {} samples ....".format(count))

    print("Done. {} samples generated.".format(count))


if __name__ == '__main__':
    main()
