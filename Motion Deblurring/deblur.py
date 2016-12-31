import numpy as np
from psf2otf import psf2otf, isodd
from blur import random_kernel

# We should regrad the image as a gray-scaled image in the following functions, and combine the result of RGB into one image.

def deblur(img, psf_shape, dim = 1):
	assert(isodd(psf_shape))
	kernel = random_kernel(psf_shape, np.random.randint(1, psf_shape[0]*psf_shape[1] - 1, dim))


def smooth_region(img, psf_shape, threshold = 5):
	(row, col) = img.shape
	hprow, hpcol = tuple(map(lambda x: int(np.floor(x/2)), psf_shape))
	window = np.zeros(img.shape)
	for x in range(row):
		for y in range(col):
			local_window = img[max(0, x - hprow):min(row, x + hprow), max(0, y - hpcol):min(col, y + hpcol)]
			t = np.std(local_window)
			if t < threshold:
				window[x, y] = 1
	return window