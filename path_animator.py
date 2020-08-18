import matplotlib.pyplot as plt


def show_path_plot(*paths):
    for path in paths:
        x = [a[0] for a in path]
        y = [a[1] for a in path]
        plt.plot(x, y)
        print(1)
    plt.show()
