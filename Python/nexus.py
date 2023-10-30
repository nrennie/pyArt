import plotnine as pn
import random
import pandas as pd
import matplotlib.colors as mcolors

def nexus(n_x, max_y, size, linewidth, bg_col, col_palette, s):
  """Generates plot of lines and points."""
  # generate data
  random.seed(s)
  max_y = max_y + 1
  plot_data=pd.DataFrame({'x': [], 'y': [], 'grp': []})
  for i in range(n_x):
      n_y_start=random.sample(range(round(max_y/2)), k=1)
      n_y_end=random.sample(range(round(max_y/2)+1, max_y), k=1)
      plot_data_i=pd.DataFrame({'x': [i]*len(range(n_y_start[0], n_y_end[0])),
      'y': range(n_y_start[0], n_y_end[0]),
      'grp': [i]*len(range(n_y_start[0], n_y_end[0]))})
      plot_data=pd.concat([plot_data, plot_data_i])
  # choose colours
  cmap=mcolors.LinearSegmentedColormap.from_list('custom_cmap', col_palette, N=len(plot_data.index))
  plot_data['col']=[mcolors.to_hex(cmap(i)) for i in range(len(plot_data.index))]
  # plot data
  p = (pn.ggplot(plot_data) +
    pn.geom_line(
      mapping=pn.aes(x="x", y="y", group="grp", colour="col"),
      size=linewidth
    ) +
    pn.geom_point(
      mapping=pn.aes(x="x", y="y", colour="col"),
      size=size
    ) +
    pn.scale_colour_identity() +
    pn.theme_void() +
    pn.theme(plot_background=pn.element_rect(fill=bg_col, colour=bg_col), panel_background=pn.element_rect(fill=bg_col, colour=bg_col)))
  return p
