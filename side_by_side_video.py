import numpy as np
import matplotlib.pyplot as plt

import argparse

from utils.image_utils import *
from utils.video_utils import *


def main():
    parser = argparse.ArgumentParser(description='Place 2 videos side by side in a single video for comparison')
    parser.add_argument('--vid_path_a', type=str, help='path to left video')
    parser.add_argument('--vid_path_b', type=str, help='path to right video')
    parser.add_argument('--fps', type=float, help='Frames per second for the output video')
    parser.add_argument('--out_path', type=str, default=None, help='path to write combined video to')
    args = parser.parse_args()

    if args.vid_path_a.endswith('.avi'):
        frames_a = load_avi(args.vid_path_a)
    else:
        frames_a = load_video_dir(args.vid_path_a)
    if len(frames_a[0].shape) == 3:
        frames_a = apply_video_transform(frames_a, convert_to_grayscale)

    if args.vid_path_b.endswith('.avi'):
        frames_b = load_avi(args.vid_path_b)
    else:
        frames_b = load_video_dir(args.vid_path_b)
    if len(frames_b[0].shape) == 3:
        frames_b = apply_video_transform(frames_b, convert_to_grayscale)

    comb_frames = [np.concatenate((a, b), axis=1) for a, b in zip(frames_a, frames_b)]

    write_video(comb_frames, args.fps, args.out_path)


if __name__ == '__main__':
    main()

# python3 side_by_side_video.py --vid_path_a EdgeLengthVideo/C3H8AirPhi1TPI1atm/C3H8AirPhi1TPI1atm.avi --vid_path_b edge_videos/canny_blur_remStatEdg\(0.25\).avi --fps 30.30 --out_path storage/tmp.avi
# python3 side_by_side_video.py --vid_path_a EdgeLengthVideo/NH3O250CSI1ATM --vid_path_b edge_videos/NH3O250CSI1ATM/canny_blur_remStatEdg\(0.1\).avi  --fps 30.30 --out_path edge_videos/NH3O250CSI1ATM/comparison.avi
