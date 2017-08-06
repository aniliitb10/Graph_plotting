import matplotlib.pyplot as plt
import numpy as np
import math

margin_x = 0.2
margin_y = 1.0
numOfTicksOnYAxis = 11
numOfTicksOnXAxis = 11
markers = ['s', 'o', 'p', '*', '8']  # ref:http://matplotlib.org/api/markers_api.html
colors = ['b', 'g', 'r', 'k', 'm']  # ref:http://matplotlib.org/api/colors_api.html
line_styles = ['-', '--', '-.', ':']  # ref:http://matplotlib.org/api/lines_api.html

counter = [0]


def plot(x, y, label="", x_label="x-axis", y_label="y-axis"):

    counter[0] += 1
    plt.plot(x, y)

    #  Fixing the length of axes
    plt.xlim((min(x) - margin_x), max(x) + margin_x)  # touple of min, max
    plt.ylim((min(y) - margin_y), max(y) + margin_y)  # touple of min, max

    #  Marking ticks on axes
    # there is a common plot.xticks in main function
    plt.yticks(np.linspace(min(y) - margin_y, max(y) + margin_y, numOfTicksOnYAxis))

    plt.plot(x, y,
             color=colors[counter[0] % len(colors)],
             marker=markers[counter[0] % len(markers)],
             linestyle=line_styles[counter[0] % len(line_styles)],
             markersize=8,
             label=label)  # for the legend

    plt.xlabel(x_label, fontsize=20)
    plt.ylabel(y_label, fontsize=20)


def main():
    x_axis = np.linspace(0, 2*np.pi, 100)  # start, stop, number of divisions
    y_axis_sin = [math.sin(x) for x in x_axis]
    y_axis_cos = [math.cos(x) for x in x_axis]
    plot(x_axis, y_axis_sin, "sin(x)")
    plot(x_axis, y_axis_cos, "cos(x)")

    plt.title("sin(x)/cos(x) Plot", fontsize=20)

    # plt.xticks: if an array of strings is provided as 2nd argument, it links with corresponding entry of 1st array
    # x_ticks_array = ["0", "pi/2", "pi", "1.5*pi", "2* pi"]
    # plt.xticks(np.linspace(0, 2*np.pi, len(x_ticks_array)), x_ticks_array),
    plt.xticks(np.linspace(0, 2*np.pi, numOfTicksOnXAxis))

    plt.grid()
    plt.legend()
    plt.show()
    plt.close()

main()
