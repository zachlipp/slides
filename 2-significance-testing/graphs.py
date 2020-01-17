from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

if __name__ == "__main__":
    np.random.seed(1337)
    mean = 0
    std = 1

    dist = np.random.normal(mean, std, size=500)
    # Vectorized rounding
    rounded = np.round_(dist, 1)

    # Plot distribution point-by-point
    fig, ax = plt.subplots()
    counts = dict()
    for i, x in enumerate(rounded):
        y = counts.get(x, 0) + 1
        plt.scatter(x, y, s=100, alpha=0.5, color="b")
        plt.xlim(-2.5, 2.5)
        plt.ylim(-1, 25)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        counts.update({x: y})
        filename = "anim/" + datetime.now().strftime("%d%H%M%S%f") + ".png"
        plt.savefig(filename)

    # Generate gif using imagemagick from command line/IPython
    # !convert -delay 5 anim/*.png figs/dist.gif

    rank = rounded.argsort()

    # Plot a small point
    fig, ax = plt.subplots()
    plt.scatter(rounded[rank][5], 0, s=100, alpha=0.5, color="b")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.xlim(-2.5, 2.5)
    plt.ylim(-1, 25)
    plt.savefig("figs/small_sample.png")

    # Plot a large point
    fig, ax = plt.subplots()
    plt.scatter(rounded[rank][-5], 0, s=100, alpha=0.5, color="b")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.xlim(-2.5, 2.5)
    plt.ylim(-1, 25)
    plt.savefig("figs/large_sample.png")

    total_counts = np.unique(rounded, return_counts=True)

    # Plot standard p-value threshold
    fig = plt.figure()
    plt.title("Standard p-value")
    sns.kdeplot(rounded, shade=True, color="b")
    plt.axvline(mean - 1.96 * std, color="r")
    plt.axvline(mean + 1.96 * std, color="r")
    plt.axis("off")
    plt.savefig("figs/standard_ps.png")

    # Plot more inclusive p-value threshold
    fig = plt.figure()
    plt.title("p > 0.05")
    sns.kdeplot(rounded, shade=True, color="b")
    plt.axvline(mean - 1 * std, color="r")
    plt.axvline(mean + 1 * std, color="r")
    plt.axis("off")
    plt.savefig("figs/larger_ps.png")

    # Plot more exclusive p-value threshold
    fig = plt.figure()
    plt.title("p < 0.05")
    sns.kdeplot(rounded, shade=True, color="b")
    plt.axvline(mean - 3 * std, color="r")
    plt.axvline(mean + 3 * std, color="r")
    plt.axis("off")
    plt.savefig("figs/smaller_ps.png")
