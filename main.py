from common.basic_io import read_file
import common.plots as plt
from common.interpolations import spline_interpolation

files = ['100.csv', 'MountEverest.csv']
basename1, basename2 = files[0].split('.')[0], files[1].split('.')[0]
nodes_count = [3,7,13,39]

data = read_file(f"2018_paths/{files[0]}")
data2 = read_file(f"2018_paths/{files[1]}")

spline_interpolation(data, 1.0)

plt.plot_track(data, basename1, basename1)
plt.plot_track(data2, basename2, basename2)

for count in nodes_count:
    plt.plot_lagrange(data, basename1, basename1, count)
    plt.plot_lagrange(data, basename1, basename1, count, 'ch')
    plt.plot_cubic_spline(data, basename1, basename1, count)
    plt.plot_lagrange(data2, basename2, basename2, count)
    plt.plot_lagrange(data2, basename2, basename2, count, 'ch')
    plt.plot_cubic_spline(data2, basename2, basename2, count)
