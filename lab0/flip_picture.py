import scipy
from scipy import ndimage
from scipy import misc
import pylab as plt
import numpy as np

img = misc.imread('lena.jpg', mode='L')
flip_lena = np.flipud(img)

plt.imshow(flip_lena, cmap=plt.cm.gray)
plt.show()