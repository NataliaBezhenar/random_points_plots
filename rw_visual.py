import matplotlib.pyplot as plt
from random_walk import RandomWalk


def set_common_conditions(axes, rw_objects_list):
    for axs in range(len(axes)):
        ax[axs].set_facecolor('black')
        ax[axs].scatter(0, 0, c='green', edgecolors='none', s=100)
        ax[axs].scatter(rw_objects_list[axs].x_values[-1], rw_objects_list[axs].y_values[-1], c='red',
                        edgecolors='none', s=100)


def create_objects(axes, points_number=500):
    rw_obj_list = []
    rws = []
    for axs in range(len(axes)):
        rw_obj_list.append(RandomWalk(points_number))
    for rw_list_object in rw_obj_list:
        rw_list_object.fill_walk()
        rws.append(rw_list_object)
    return rws


while True:
    fig, ax = plt.subplots(4, 1)
    fig.suptitle("Random walking plots", fontsize=16)
    fig.set_figwidth(10)
    fig.set_figheight(10)
    rw_list = create_objects(ax)

    for i in range(len(ax)):
        if (i + 1) % 4 == 0:
            ax[i].scatter(rw_list[i].x_values, rw_list[i].y_values, marker='X', c=list(range(rw_list[i].num_points)),
                          cmap=plt.cm.plasma, edgecolor='none', s=40)
        elif (i + 1) % 3 == 0:
            ax[i].scatter(rw_list[i].x_values, rw_list[i].y_values, marker='o', c=list(range(rw_list[i].num_points)),
                          cmap=plt.cm.RdPu, edgecolor='none', s=40)
        elif (i + 1) % 2 == 0:
            ax[i].scatter(rw_list[i].x_values, rw_list[i].y_values, marker='*', c=list(range(rw_list[i].num_points)),
                          cmap=plt.cm.Oranges, edgecolor='none', s=40)
        else:
            ax[i].scatter(rw_list[i].x_values, rw_list[i].y_values, c=list(range(rw_list[i].num_points)),
                          cmap=plt.cm.Blues, edgecolor='none', s=16)

    set_common_conditions(ax, rw_list)
    plt.show()

    keep_running = input("Another walk?(y/n):")
    if keep_running == 'n':
        break
