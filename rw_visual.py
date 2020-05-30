import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(500)
    rw.fill_walk()
    fig, ax = plt.subplots(4, 1)
    point_numbers = list(range(rw.num_points))
    ax[0].scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=16)
    # Highlighting of the first and last points
    ax[0].scatter(0, 0, c='green', edgecolors='none', s=100)
    ax[0].scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax[0].set_title("Random walking plots")
    ax[0].set_facecolor('black')
    # Hide axis
    ax[0].get_xaxis().set_visible(False)
    ax[0].get_yaxis().set_visible(False)
    fig.set_figwidth(10)
    fig.set_figheight(10)

    plt.show()
    keep_running = input("Another walk?(y/n):")
    if keep_running == 'n':
        break
