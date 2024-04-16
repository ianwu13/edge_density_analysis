import numpy as np
import cv2 as cv

import argparse

from utils.image_utils import *
from utils.video_utils import *
from utils.edge_detection import *


def main():
    parser = argparse.ArgumentParser(description='Take an image and display detected edges')
    parser.add_argument('--img_path', type=str, help='path to image file')
    args = parser.parse_args()

    img = load_3chan_img(args.img_path)
    edges = canny_edge_det(img)
    display_img_arr(edges)


if __name__ == '__main__':
    main()


# EXAMPLE CALLS:
# python3 img_to_edges.py --img_path EdgeLengthVideo/C3H8AirPhi1TPI1atm/image\!3070.tif
