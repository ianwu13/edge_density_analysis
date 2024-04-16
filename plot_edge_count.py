import numpy as np
import matplotlib.pyplot as plt

import argparse

from utils.image_utils import *
from utils.video_utils import *


def main():
    parser = argparse.ArgumentParser(description='Plot number of edge pixels over time')
    parser.add_argument('--avi_path', type=str, help='path to video file')
    parser.add_argument('--out_path', type=str, default=None, help='path to write plot to')
    args = parser.parse_args()

    frames = load_avi(args.avi_path)
    if len(frames[0].shape) == 3:
        frames = apply_video_transform(frames, convert_to_grayscale)
    
    pix_count = frames[0].shape[0] * frames[0].shape[1]

    edges_over_time = [np.count_nonzero(f)/pix_count for f in frames]
    
    # Plot
    plt.plot(edges_over_time)
    plt.title(f'Edge Ration Over Time for {args.avi_path}')
    plt.xlabel('Frame')
    plt.ylabel('Percent of Pixels Tagged as an Edge')
    plt.ylim(0, 1)
    plt.savefig(args.out_path)


if __name__ == '__main__':
    main()

# python3 plot_edge_count.py --avi_path edge_videos/canny.avi --out_path storage/plots/canny.png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_x_blur.avi --out_path storage/plots/sobel_x_blur.png
# python3 plot_edge_count.py --avi_path edge_videos/canny_blur.avi --out_path storage/plots/canny_blur.png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_xy.avi --out_path storage/plots/sobel_xy.png
# python3 plot_edge_count.py --avi_path edge_videos/canny_blur_remStatEdg\(0.25\).avi --out_path storage/plots/canny_blur_remStatEdg\(0.25\).png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_xy_blur.avi --out_path storage/plots/sobel_xy_blur.png
# python3 plot_edge_count.py --avi_path edge_videos/canny_remStatEdg\(0.25\).avi --out_path storage/plots/canny_remStatEdg\(0.25\).png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_y.avi --out_path storage/plots/sobel_y.png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_x.avi --out_path storage/plots/sobel_x.png
# python3 plot_edge_count.py --avi_path edge_videos/sobel_y_blur.avi --out_path storage/plots/sobel_y_blur.png
