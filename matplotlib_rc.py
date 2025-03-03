import matplotlib.pyplot as plt
import matplotlib as mpl

dpi = 100 #decided by display device

default_text_size_points = 10
default_line_width_points = 1

# matplotlib rules
mpl_points_per_inch = 72
mpl_pixels_per_point = dpi / mpl_points_per_inch

line_width_pixels = 1
line_width_points = line_width_pixels / mpl_pixels_per_point
plt.rcParams['lines.linewidth'] = line_width_points
_lw = line_width_points

text_size_points = default_text_size_points
plt.rcParams['font.size'] = text_size_points

plt.rcParams['figure.dpi'] = dpi

plt.rcParams['toolbar'] = 'None'
plt.rcParams['axes.xmargin'] = 0

if True:
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['green'],alpha=[0.66])
    plt.rcParams['figure.facecolor'] = 'whitesmoke'
    #plt.rcParams['figure.facecolor'] = 'lightgrey'
    plt.rcParams['axes.facecolor'] = 'whitesmoke'
else:
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=['yellow'],alpha=[1])
    mpl.rcParams["figure.facecolor"] = "black"
    mpl.rcParams["axes.facecolor"] = "black"
    mpl.rcParams["axes.edgecolor"] = "whitesmoke"