import numpy as np
import cv2 as cv 


def canny_edge_det(img: np.ndarray, t1=50, t2=100) -> np.ndarray:
	# Canny edge detection: gradient based
    # void cv::Canny 	( 	InputArray  	image,
	# 	OutputArray  	edges,
	# 	double  	threshold1,
	# 	double  	threshold2,
	# 	int  	apertureSize = 3,
	# 	bool  	L2gradient = false 
	# )
	return cv.Canny(image=img, threshold1=t1, threshold2=t2)


def sobel_x(img: np.ndarray) -> np.ndarray:
	# Sobel (Kernel application) Edge Detection on the X axis
	edges = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5).astype(np.uint8)
	return cv.cvtColor(edges, cv.COLOR_BGR2GRAY)


def sobel_y(img: np.ndarray) -> np.ndarray:
	# Sobel (Kernel application) Edge Detection on the Y axis
	edges = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5).astype(np.uint8)
	return cv.cvtColor(edges, cv.COLOR_BGR2GRAY)


def sobel_xy(img: np.ndarray) -> np.ndarray:
	# Combined X and Y Sobel (Kernel application) Edge Detection
	edges = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5).astype(np.uint8)
	return cv.cvtColor(edges, cv.COLOR_BGR2GRAY)


EDGE_DET_ALGS = {
	'canny': canny_edge_det,
	'sobel_x': sobel_x,
	'sobel_y': sobel_y,
	'sobel_xy': sobel_xy,
}
