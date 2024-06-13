import matplotlib.pyplot as plt
from common.common import *
from common.interpolations import *
def plot_track(points, name, savename):
    x_coords, y_coords = zip(*points)

    plt.figure(figsize=(8, 6));
    plt.plot(x_coords, y_coords, linewidth=1, linestyle='-', color='blue', label=name)

    plt.xlabel('Dystans (m)')
    plt.ylabel('Wysokość (m)')
    plt.title(f"Trasa {name}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{savename}",dpi=300)


def plot_lagrange(points, name, savename, num_of_nodes, method='lin'):
    if method == 'lin':
        nodes_indexes = linear_space(0, len(points) - 1, num_of_nodes)
    elif method == 'ch':
        nodes_indexes = chebyshev_space(0, len(points) - 1, num_of_nodes)
    else:
        raise RuntimeError();

    interpolation_nodes = [points[int(i)] for i in nodes_indexes]

    x_coords, y_coords = zip(*points)

    y_interpolated = [lagrange_interpoplation(interpolation_nodes, x) for x in x_coords]

    plt.figure(figsize=(8, 6))
    plt.subplot(1,1,1)
    plt.plot(x_coords, y_coords, linewidth=1, linestyle='-', color='blue', label=name)
    plt.plot(x_coords, y_interpolated, linewidth=1, linestyle='-', color='red', label='Interpolacja Lagrange')
    plt.scatter([node[0] for node in interpolation_nodes], [node[1] for node in interpolation_nodes], zorder=2, label="Węzły interpolacji")

    plt.xlabel('Dystans (m)')
    plt.ylabel('Wysokość (m)')
    plt.title(f"Trasa {name} - interpolacja Lagrange na {num_of_nodes} węzłach (dystrybucja {'liniowa' if method=='lin' else 'Chebysheva'})")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{savename}_{num_of_nodes}_{method}_lagrange",dpi=300)
    plt.close()

    mse = calculate_mse(y_coords, y_interpolated)
    print(f"{savename}_{num_of_nodes}_{method}_lagrange MSE: {mse}")


def plot_cubic_spline(points, name, savename, num_of_nodes):
    nodes_indexes = linear_space(0, len(points) - 1, num_of_nodes)
    interpolation_nodes = [points[int(i)] for i in nodes_indexes]

    x_coords, y_coords = zip(*points)

    y_interpolated = [spline_interpolation(interpolation_nodes, x) for x in x_coords]

    plt.figure(figsize=(8, 6))
    plt.subplot(1,1,1)
    plt.plot(x_coords, y_coords, linewidth=1, linestyle='-', color='blue', label=name)
    plt.plot(x_coords, y_interpolated, linewidth=1, linestyle='-', color='red', label='Interpolacja splajnami')
    plt.scatter([node[0] for node in interpolation_nodes], [node[1] for node in interpolation_nodes], zorder=2, label="Węzły interpolacji")

    plt.xlabel('Dystans (m)')
    plt.ylabel('Wysokość (m)')
    plt.title(f"Trasa {name} - interpolacja splajnami trzeciego stopnia na {num_of_nodes} węzłach")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{savename}_{num_of_nodes}_spline",dpi=300)
    plt.close()
    mse = calculate_mse(y_coords, y_interpolated)
    print(f"{savename}_{num_of_nodes}_spline MSE: {mse}")
