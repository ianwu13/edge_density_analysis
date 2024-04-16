import os

import numpy as np
import cv2 as cv
from tqdm import tqdm


# Expects a directory path, files should be in format image!<INDEX>.tif
def load_video_dir(dir_path:str):
    dir_content = os.listdir(dir_path)
    tifs = filter(lambda f: f.endswith('.tif'), dir_content)
    tifs = sorted(tifs, key=lambda n: int(n.split('.')[0].split('!')[1]))
    tif_paths = map(lambda t: '/'.join([dir_path, t]), tifs)
    return np.array([cv.imread(img_path) for img_path in tif_paths])


def load_avi(path:str):
    cap = cv.VideoCapture(path)
    frames = []
    while cap.isOpened():
        ret, f = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            break
        frames.append(f)
        
    cap.release()
    return np.array(frames)


def apply_video_transform(frames:np.array, transform_function):
    return np.array([transform_function(f) for f in tqdm(frames)])


def write_video(frames:np.array, fps:int, path:str):
    assert path.endswith('.avi'), "only writing to .avi files is currently supported"

    # Make sure destination path exists
    dir_path = '/'.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Initialize video writer object
    frame_size = (frames[0].shape[1], frames[0].shape[0])
    vid_writer = cv.VideoWriter(path, cv.VideoWriter_fourcc('M','J','P','G'), fps, frame_size, isColor=False)
    # vid_writer = cv.VideoWriter(path, -1, fps, frame_size)

    for f in frames:
        vid_writer.write(f)
        # vid_writer.write(np.array([f, f, f]))

    vid_writer.release()


# Assumes frames are single channel (grayscale) and binary (0 || 255)
def remove_static_edges(frames:np.array, ratio:float=0.25):
    shape = frames[0].shape
    frame_count = len(frames)

    for i in range(shape[0]):
        for j in range(shape[1]):
            pix_ts = frames[:, i, j]
            on_count = np.count_nonzero(pix_ts)
            if (on_count / frame_count) > ratio:
                frames[:, i, j] = 0
    
    return frames
