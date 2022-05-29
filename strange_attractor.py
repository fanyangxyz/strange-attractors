import sys

from matplotlib import pyplot as plt
import numpy as np
import gflags

gflags.DEFINE_integer('init', 1000, '')
gflags.DEFINE_integer('iter', 10000, '')
gflags.DEFINE_string('name', None, '')
gflags.DEFINE_boolean('use_line', True, '')
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


def main():
    x = 0.1
    y = 0.1

    for i in range(FLAGS.init):
        x, y = compute(x, y)
    print('initialized')

    xs, ys = [], []
    for i in range(FLAGS.iter):
        x, y = compute(x, y)
        xs.append(x)
        ys.append(y)

    plt.figure(figsize=(16, 16))
    if FLAGS.use_line:
        plt.plot(xs, ys, alpha=0.15, linewidth=0.05, c='black')
    else:
        plt.style.use('dark_background')
        plt.scatter(xs, ys, alpha=0.25, linewidth=0, c='white')
    # plt.show()
    plt.axis('off')
    plt.savefig('plot.png' if not FLAGS.name else f'{FLAGS.name}.png')


if __name__ == "__main__":
    FLAGS(sys.argv)
    main()
