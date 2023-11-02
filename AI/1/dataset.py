import numpy as np
import sys, os
sys.path.append('/Users/minchan/Documents/GitHub/coding_test_python/AI/1/dataset')
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# (x_train, t_train),(x_test, t_test) = load_mnist(flatten=True, normalize=False)
(x_train, t_train),(x_test, t_test) = load_mnist(flatten=True, normalize=False, one_hot_label=True)

img = x_train[0]
lable = t_train[0]
print(lable)
print(img)

img = np.reshape(28, 28)

print(img.shape)
img_show(img)