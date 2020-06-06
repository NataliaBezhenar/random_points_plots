import matplotlib.pyplot as plt
from random_walk import RandomWalk

def set_common_conditions(ax):
    for i in range(len(ax)):
        ax[i].set_facecolor('black')
        ax[i].scatter(0, 0, c='green', edgecolors='none', s=100)


while True:
    rw = RandomWalk(500)
    rw1 = RandomWalk(500)
    rw2 = RandomWalk(500)
    rw3 = RandomWalk(500)
    rw.fill_walk()
    rw1.fill_walk()
    rw2.fill_walk()
    rw3.fill_walk()
    fig, ax = plt.subplots(4, 1)
    fig.suptitle("Random walking plots", fontsize=16)
    point_numbers = list(range(rw.num_points))
    ax[0].scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=16)
    # Highlighting of the first and last points
    ax[0].scatter(0, 0, c='green', edgecolors='none', s=100)
    ax[0].scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    fig.set_figwidth(10)
    fig.set_figheight(10)

    set_common_conditions(ax)

    ax[1].scatter(rw1.x_values, rw1.y_values, marker='*', c=point_numbers, cmap=plt.cm.Oranges, edgecolor='none', s=40)
    ax[2].scatter(rw2.x_values, rw2.y_values, marker='o', c=point_numbers, cmap=plt.cm.RdPu, edgecolor='none', s=40)
    ax[3].scatter(rw3.x_values, rw3.y_values, marker='X', c=point_numbers, cmap=plt.cm.plasma, edgecolor='none', s=40)

    ax[1].scatter(0, 0, c='green', edgecolors='none', s=100)
    ax[1].scatter(rw1.x_values[-1], rw1.y_values[-1], c='red', edgecolors='none', s=100)
    ax[2].scatter(0, 0, c='green', edgecolors='none', s=100)
    ax[2].scatter(rw2.x_values[-1], rw2.y_values[-1], c='red', edgecolors='none', s=100)
    ax[3].scatter(0, 0, c='green', edgecolors='none', s=100)
    ax[3].scatter(rw3.x_values[-1], rw3.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()
    keep_running = input("Another walk?(y/n):")
    if keep_running == 'n':
        break
