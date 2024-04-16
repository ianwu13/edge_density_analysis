import numpy as np
import cv2 as cv


def load_gs_img(path: str):
    img = cv.imread(path)
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.uint8)


def load_3chan_img(path: str):
    return cv.imread(path).astype(np.uint8)


def convert_to_grayscale(img: np.array):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY).astype(np.uint8)


def preview_img(path: str):
    img = cv.imread(path)
    cv.imshow('Preview', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def display_img_arr(arr: np.ndarray):
    cv.imshow('Preview', arr)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Blur
def gaussian_blur(arr: np.ndarray, kernel_shape=(3,3), sx=0, sy=0):
    return cv.GaussianBlur(arr, kernel_shape, sigmaX=sx, sigmaY=sy)


# Contrast enhancement
def histogram_equalization(arr: np.ndarray):
    pass  # TODO
    # return cv.GaussianBlur(arr, (3,3), sigmaX=0, sigmaY=0)


def decrease_range(arr: np.ndarray, upper=185, lower=70):
    band = upper - lower
    equalizer = np.vectorize(lambda x: 0 if x < lower else (255 if x > upper else ((x - lower) * 255 / band)))
    return equalizer(arr).astype(np.uint8)


# Noise Removal
def fast_denoising(arr: np.ndarray):
    denoised = cv.fastNlMeansDenoising(arr, None, 20, 7, 21)
    denoised[np.where(denoised >= 200)] = 255
    denoised[np.where(denoised < 200)] = 0
    return denoised


def remove_pt_noise(arr: np.ndarray):
    pass  # TODO
    # return cv.GaussianBlur(arr, (3,3), sigmaX=0, sigmaY=0)


DENOISING_ALGS = {
    'fast_denoising': fast_denoising,
    'remove_pt_noise': remove_pt_noise,
}
