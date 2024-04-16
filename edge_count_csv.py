import os
import numpy as np
import pandas as pd

import argparse

from utils.image_utils import *
from utils.video_utils import *


def main():
    parser = argparse.ArgumentParser(description='Get pixel count for vides in a dir')
    parser.add_argument('--dir_path', type=str, help='path to directory of videos')
    parser.add_argument('--out_path', type=str, default=None, help='path to write csv to')
    args = parser.parse_args()

    avis = os.listdir(args.dir_path)
    avis = list(filter(lambda x: x.endswith('.avi'), avis))
    avis = list(filter(lambda x: not x.startswith('comparison'), avis))  # This is dumb

    df_dict = {}
    video_lens = []
    for avi in avis:
        frames = load_avi('/'.join([args.dir_path, avi]))
        video_lens.append(len(frames))

        if len(frames[0].shape) == 3:
            frames = apply_video_transform(frames, convert_to_grayscale)
        
        df_dict['_'.join(avi.split('.')[:-1])] = [np.count_nonzero(f) for f in frames]

    assert len(set(video_lens)) == 1, f'Video must all be of same length, Found videos of lengths {set(video_lens)}'
    df_dict['frame'] = list(range(video_lens[0]))

    df = pd.DataFrame(df_dict)
    df.to_csv(args.out_path, index=False)


if __name__ == '__main__':
    main()
