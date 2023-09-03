import plotnine as pn
import numpy as np
import pandas as pd
import random
from itertools import product

# Function to generate single square of data
def crosshatch_square(s, n_lines, line_overlap, line_slope, line_col, x_start, y_start):
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
  return plot_data
    
# Function to generate grid
def crosshatch(n_x, n_y, n_lines, line_overlap, line_slope, col_palette, bg_col, linewidth, s):
  # generate data
  random.seed(s)
  grid_product = product(list(range(n_x)), list(range(n_y)))
  grid_data = pd.DataFrame(grid_product, columns=['x_start', 'y_start'])
  grid_data['line_col'] = random.choices(col_palette, k=n_x*n_y)
  all_data = pd.DataFrame()
  for i in range(n_x*n_y):
    i_data = crosshatch_square(s=i, n_lines=n_lines, line_overlap=line_overlap, line_slope=line_slope, line_col=grid_data['line_col'][i], x_start=grid_data['x_start'][i], y_start=grid_data['y_start'][i])
    all_data = pd.concat([all_data, i_data])
  # plot
  p = (pn.ggplot() +
  pn.geom_segment(
        data = all_data,
        mapping = pn.aes(
          x = "x_bottom", xend = "x_top",
          y = "y_bottom", yend = "y_top",
          alpha = "alpha", group = "grp",
          colour = "line_col"
        ),
        size = linewidth
      ) +
      pn.scale_colour_identity() +
      pn.scale_alpha_continuous(guide=False) +
      pn.coord_fixed(expand=False) +
      pn.theme_void() +
      pn.theme(plot_background=pn.element_rect(fill=bg_col), plot_margin=None, figure_size = (10, 10)))
  return p

# Example
crosshatch(n_x=10, n_y=10, n_lines=50, line_overlap=0.2, line_slope=0.2, col_palette=["#413C58", "#D1495B", "#EDAE49", "#00798C", "#003D5B"], bg_col="#FAFAFA", linewidth=0.1, s=123)
