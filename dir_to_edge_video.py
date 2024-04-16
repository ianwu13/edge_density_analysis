import numpy as np
import cv2 as cv

import argparse

from utils.image_utils import *
from utils.video_utils import *
from utils.edge_detection import *


def main():
    parser = argparse.ArgumentParser(description='Take a video and convert to edges video')
    parser.add_argument('--dir_path', type=str, help='path to directory for video')
    parser.add_argument('--fps', type=float, help='frames per second for the video')
    parser.add_argument('--out_path', type=str, default=None, help='path to write edges video')
    # Image transformation/edge detection
    parser.add_argument('--increase_contrast', type=int, nargs=2, default=None, help='Boost Contrast before applying edge detection. Accepts 2 arguments in the form "UPPER_BOUND LOWER_BOUND" NOTE: this is relatively compute-intensive')
    parser.add_argument('--blur', action='store_true', help='Apply a gaussian blur before edge detection')
    parser.add_argument('--edge_det_alg', type=str, default='canny', choices=EDGE_DET_ALGS.keys(), help='Edge detection algorithm to use')
    parser.add_argument('--static_edges_threshold', type=float, default=None, help='Remove static edges')
    parser.add_argument('--denoising_alg', type=str, default=None, choices=DENOISING_ALGS.keys(), help='Denoising algorithm to apply after static edge removal')

    args = parser.parse_args()

    frames = load_video_dir(args.dir_path)

    # Increase contrast if called
    if args.increase_contrast:
        print('INCREASING CONTRAST')
        frames = [decrease_range(f, upper=args.increase_contrast[1], lower=args.increase_contrast[0]) for f in frames]

    # Apply blur if called
    if args.blur:
        print('BLURRING')
        frames = apply_video_transform(frames, gaussian_blur)

    # Detect edges
    print('DETECTING EDGES')
    eda = EDGE_DET_ALGS[args.edge_det_alg]
    edge_frames = np.array([eda(f) for f in frames])

    # Remove static edges if specified
    if args.static_edges_threshold:
        print('REMOVING STATIC EDGES')
        edge_frames = remove_static_edges(edge_frames, args.static_edges_threshold)

    # Remove noise if specified
    if args.denoising_alg:
        print('DENOISING')
        da = DENOISING_ALGS[args.denoising_alg]
        edge_frames = apply_video_transform(edge_frames, da)

    # generate output path if not specified
    if args.out_path is None:
        out_comps = [f'edge_videos/{args.dir_path.split("/")[-1]}/{args.edge_det_alg}']
        if args.increase_contrast: out_comps.append(f'_increaseContrast_{args.increase_contrast[0]}_{args.increase_contrast[1]}')
        if args.blur: out_comps.append('_blur')
        if args.static_edges_threshold: out_comps.append(f'_remStatEdg_{str(args.static_edges_threshold).replace(".", "pt")}')
        if args.denoising_alg: out_comps.append(f'_denoised_{args.denoising_alg}')
        out_comps.append('.avi')
        out_path = ''.join(out_comps)
    else:
        out_path = args.out_path
    print(f'SAVING - {out_path}')
    # Save video
    write_video(edge_frames, args.fps, out_path)


if __name__ == '__main__':
    main()


# EXAMPLE CALLS:
# python3 dir_to_edge_video.py --dir_path EdgeLengthVideo/C3H8AirPhi1TPI1atm --fps 30.30 --edge_det_alg
# python3 dir_to_edge_video.py --fps 30.30 --dir_path EdgeLengthVideo/NH3O250CSI1ATM --edge_det_alg
# python3 dir_to_edge_video.py --fps 30.30 --dir_path EdgeLengthVideo/NH3O250TPI1ATM --edge_det_alg
