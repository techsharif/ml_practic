# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
import numpy as np

a = np.arange(15)
print(a)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

a = a.reshape(3, 5)  # error: a.reshape(3, 4) or a.reshape(3, 6)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

print(a.shape)  # (3, 5)
print(a.ndim)  # 2
