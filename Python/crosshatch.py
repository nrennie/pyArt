import plotnine as pn
import PrettyCols as pc
import numpy as np
import pandas as pd
import random

# set parameters
s = 123
n_lines = 10
line_overlap = 0.1
line_slope = 0.1
line_col = 'blue'
x_start = 0
y_start = 0

s = np.random.uniform(0, 1, n_lines)

# generate data
random.seed(s)
# vertical lines
d_vert_lines = {'x_bottom': np.random.uniform(0, 1, n_lines),
'y_bottom': np.random.uniform(0 - line_overlap, 0, n_lines),
'y_top': np.random.uniform(1, 1 + line_overlap, n_lines),
'alpha': np.random.uniform(0, 1, n_lines),
'grp': list(map(str, list(range(n_lines)))),
'line_col': [line_col] * n_lines}
vert_lines = pd.DataFrame(data=d_vert_lines)
vert_lines['x_top'] = vert_lines['x_bottom'] + np.random.uniform(-1 * line_slope, line_slope, n_lines)

# horizontal lines
d_horiz_lines = {'y_bottom': np.random.uniform(0, 1, n_lines),
'x_bottom': np.random.uniform(0 - line_overlap, 0, n_lines),
'x_top': np.random.uniform(1, 1 + line_overlap, n_lines),
'alpha': np.random.uniform(0, 1, n_lines),
'grp': list(map(str, list(range(n_lines)))),
'line_col': [line_col] * n_lines}
horiz_lines = pd.DataFrame(data=d_horiz_lines)
horiz_lines['y_top'] = horiz_lines['y_bottom'] + np.random.uniform(-1 * line_slope, line_slope, n_lines)

# join data
plot_data = pd.concat([vert_lines, horiz_lines])
plot_data['x_bottom'] = plot_data['x_bottom'] + x_start
plot_data['y_bottom'] = plot_data['y_bottom'] + y_start
plot_data['x_top'] = plot_data['x_top'] + x_start
plot_data['y_top'] = plot_data['y_top'] + y_start

# plot
(pn.ggplot() +
pn.geom_segment(
      data = plot_data,
      mapping = pn.aes(
        x = "x_bottom", xend = "x_top",
        y = "y_bottom", yend = "y_top",
        alpha = "alpha", group = "grp",
        colour = "line_col"
      )
    ) +
    pn.scale_colour_identity() +
    pn.scale_alpha_continuous(guide=False) +
    pn.coord_fixed() +
    pn.theme_void()) 
    
#TODO: multiple squares data
#TODO: set colours
