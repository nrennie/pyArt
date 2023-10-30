import plotnine as pn

# Crosshatch
import Python.crosshatch as crosshatch
p = crosshatch.crosshatch(n_x=10, n_y=10, n_lines=50, line_overlap=0.2, line_slope=0.2, col_palette=["#413C58", "#D1495B", "#EDAE49", "#00798C", "#003D5B"], bg_col="#121212", linewidth=0.1, interpolate=True, s=123)
pn.ggsave(p, filename="Images/crosshatch.png", height=4, width=4, dpi=300)

