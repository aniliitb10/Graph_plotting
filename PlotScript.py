import matplotlib.pyplot as plt
import numpy as np
import math

margin_x = 0.0
margin_y = 1.0
numOfTicksOnYAxis = 11
numOfTicksOnXAxis = 11
font_size = 20
markers = ['s', 'o', 'p', '*', '8']  # ref:http://matplotlib.org/api/markers_api.html
colors = ['b', 'g', 'r', 'k', 'm']  # ref:http://matplotlib.org/api/colors_api.html
line_styles = ['-', '--', '-.', ':']  # ref:http://matplotlib.org/api/lines_api.html
counter = [0]


def plot(x, y, label=""):

    counter[0] += 1
    plt.plot(x, y)

    plt.plot(x, y,
             color=colors[counter[0] % len(colors)],
             marker=markers[counter[0] % len(markers)],
             linestyle=line_styles[counter[0] % len(line_styles)],
             markersize=8,
             label=label)  # for the legend


def main():
    x_axis = np.linspace(0, 2*np.pi, 100)  # start, stop, number of divisions
    y_axis_sin = [math.sin(x) for x in x_axis]
    y_axis_cos = [math.cos(x) for x in x_axis]
    y_axis_cos2x = [math.cos(2*x) for x in x_axis]

    plot(x_axis, y_axis_sin, "sin(x)")
    plot(x_axis, y_axis_cos, "cos(x)")
    plot(x_axis, y_axis_cos2x, "cos(2x)")

    min_x, max_x = min(x_axis), max(x_axis)
    min_y, max_y = min(min(y_axis_sin), min(y_axis_cos)), max(max(y_axis_sin), max(y_axis_cos))

    # draw y = 0
    plt.plot([min_x - margin_x, max_x + margin_x], [0, 0], color='k')

    # draw x = 0 line
    # plt.plot([0, 0], [min_y - margin_y, max_y + margin_y], color='k')

    #  Fixing the length of axes
    plt.xlim(min_x - margin_x, max_x + margin_x)  # touple of min, max
    plt.ylim(min_y - margin_y, max_y + margin_y)  # touple of min, max

    #  Marking ticks on axes
    plt.yticks(np.linspace(min_y - margin_y, max_y + margin_y, numOfTicksOnYAxis))

    # plt.xticks: if an array of strings is provided as 2nd argument, it links with corresponding entry of 1st array
    # x_ticks_array = ["0", "pi/2", "pi", "1.5*pi", "2* pi"]
    # plt.xticks(np.linspace(0, 2*np.pi, len(x_ticks_array)), x_ticks_array),
    plt.xticks(np.linspace(0, 2*np.pi, numOfTicksOnXAxis))

    plt.xlabel("x-values (in radian)", fontsize=font_size)
    plt.ylabel("Values", fontsize=font_size)
    plt.title("sin(x), cos(x) and cos(2x)", fontsize=font_size)

    plt.grid()
    plt.legend()
    plt.show()
    plt.close()

main()
