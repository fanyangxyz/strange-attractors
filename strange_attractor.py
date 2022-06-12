import sys

from matplotlib import pyplot as plt
import numpy as np
import gflags
from PIL import Image

gflags.DEFINE_integer('init', 1000, '')
gflags.DEFINE_integer('iter', 10000, '')
gflags.DEFINE_string('name', None, '')
FLAGS = gflags.FLAGS


def compute(x, y):
    # coefficients for "The King's Dream
    a = -0.966918
    b = 2.879879
    c = 0.765145
    d = 0.744728
    x_new = np.sin(y * b) + c * np.sin(x * b)
    y_new = np.sin(x * a) + d * np.sin(y * a)
    return x_new, y_new


def impl(x, y, s, a, cs):
    xs, ys = [], []
    for i in range(FLAGS.iter):
        x, y = compute(x, y)
        xs.append(x)
        ys.append(y)
    plt.scatter(xs, ys, s=s, alpha=a, linewidth=0, edgecolors='none', c=cs)
    return x, y


def main(palette, x, y, name):

    for i in range(FLAGS.init):
        x, y = compute(x, y)
    print('initialized')

    with open(palette, 'rb') as f:
        colors = np.load(f) / 255.

    plt.figure(figsize=(16, 16))
    for i in range(3):
        s = 2**(10 + i)
        a = 0.8
        cs = colors[np.random.randint(0, len(colors), size=(FLAGS.iter,))]
        x, y = impl(x, y, s, a, cs)
    # plt.show()
    plt.axis('off')
    plt.savefig(name)
    plt.close()


def driver():
    np.random.seed(32)
    for i in range(32):
        palette = f'/Users/fanyang/code/minGPT/palettes/palette_{i}.npy'
        x = np.random.random()
        y = np.random.random()
        base_name = FLAGS.name if FLAGS.name else 'plot'
        name = f'{base_name}_{i}.png'
        main(palette, x, y, name)
        # break


if __name__ == "__main__":
    FLAGS(sys.argv)
    driver()
