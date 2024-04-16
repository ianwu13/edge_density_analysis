# Edge Density Measurement

Code for measuring explosion edge density from videos.

## Generating Edge Videos

Edge videos can be generated with the `dir_to_edge_video.py` script. General descriptions of arguments for this script can be found by running `python3 dir_to_edge_video.py -h`, but more in depth descriptions are provided below.

- "--dir_path": Path to a directory containing .tif files corresponding to the frames of a video. It is assumed that these files are names in the format "arbitrary!\[NUM\].tif", where \[NUM\] corresponds to the order of frames, although it does not necessarily need to start at 0.
- "--fps": Frames per second at which to output the edge video
- "--out_path": Specifies where to save the output video, must be a ".avi" file. If not specified (Recommended), a path and filename will be automatically generated. This filename will indicate which transformations have been applied to generate the video.

- "--increase_contrast": If specified, this will increase the contrast of each image before applying further transformations. This can make it easier for the edge detection algorithm to detect soft/unclear edges but is fairly compute-intensive. This argument accepts 2 arguments, the first being the lower boud for the mapping and the second being the upper bound. For example, to set the lower and upper bounds to 75 and 180, respectively, the argument would be passed as "--increase_contrast 75 180" This mapping is shown in the figure below.
![](/assets/inc_contrast_plots.png)

- "--blur": A binary argument. If specified, a blur will be applied to the frames before edge detection, which can reduce false positives and improve performance.
- "--edge_det_alg": Specifies the edge detection algorithm to run. In most cases, this should be set to "canny".
- "--static_edges_threshold": Sets the threshold to use for removing static edges in the output video. For example, "--static_edges_threshold 0.1" will remove edges for pixels that are found to be edge pixels for more than 10% of the video. If this argument is not set, static edges are not removed.
- "--denoising_alg": Specifies the denoising algorithm to use. If not set, denoising is not applied. This process is fairly compute-intensive, so this can take a long time to run for videos with many frames.


## Functions with Parameters to Adjust

`image_utils.py`

- TODO

`video_utils.py`

- TODO

`edge_detection.py`

- TODO
