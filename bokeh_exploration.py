from bokeh.plotting import figure, show
from bokeh.plotting import output_file
# from bokeh.plotting import save
from bokeh.models import BoxAnnotation
from bokeh.io import curdoc
from bokeh.models import NumeralTickFormatter
from datetime import datetime, timedelta
# from bokeh.layouts import row
from bokeh.layouts import gridplot

# ---------------------------------------------------------------------------------------
#  prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

#  generate list of dates (today's date in subsequent weeks)
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]

#  apply theme to current document
# Bokeh comes with five built-in themes: caliber, dark_minimal, light_minimal, night_sky, contrast.
curdoc().theme = "light_minimal"

#  create a new plot with a title and axis labels
p = figure(
    title="Simple line example",
    x_axis_label='x',
    y_axis_label='y',
    y_range=(0, 10),
    toolbar_location="below",
    )
# p = figure(sizing_mode="stretch_width", max_width=500, height=250)

#  format axes ticks
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")

#  change headline location to the left
p.title_location = "left"

#  style the headline
p.title.text_font_size = "25px"
p.title.align = "right"
p.title.background_fill_color = "darkgrey"
p.title.text_color = "white"


#  add multiple renderers
p.line(x, y1, legend_label="Temp.", line_color="blue", line_width=2)
p.line(x, y2, legend_label="Rate", line_color="red", line_width=2)
# p.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")
p.line(x, y3, legend_label="Objects", line_color="green", line_width=2)
# p.circle(x, y3, legend_label="Objects", line_color="yellow", size=12)
"""
circle = p.circle(
    x,
    y3,
    legend_label="Objects",
    fill_color="red",
    fill_alpha=0.5,
    line_color="blue",
    size=80,
)

#  change color of previously created object's glyph
glyph = circle.glyph
glyph.fill_color = "blue"
"""

#  add bands to the y-grid
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

#  change just some things about the x-grid
p.xgrid.grid_line_color = "red"

#  change just some things about the y-grid
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]

#  change some things about the x-axis
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

#  change some things about the y-axis
p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

#  display legend in top left corner (default is top right corner)
# p.legend.location = "top_left"

#  add a title to your legend
p.legend.title = "Obervations"

#  change appearance of legend text
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"

#  change border and background of legend
p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.8
p.legend.background_fill_color = "navy"
p.legend.background_fill_alpha = 0.2

#  add box annotations
low_box = BoxAnnotation(top=2, fill_alpha=0.1, fill_color="red")
# mid_box = BoxAnnotation(bottom=80, top=180, fill_alpha=0.1, fill_color="green")
high_box = BoxAnnotation(bottom=8, fill_alpha=0.1, fill_color="red")

#  add boxes to existing figure
p.add_layout(low_box)
# p.add_layout(mid_box)
p.add_layout(high_box)

#  show the results
show(p)
output_file(filename="bokeh_exploration.html", title="Static HTML file")
# save(p)
# exit()
# ------------------------------------------------------------------
#  create three plots with one renderer each
s1 = figure(width=250, height=250)  # background_fill_color="# fafafa")
s1.circle(x, y1, size=12, color="#53777a", alpha=0.8)

s2 = figure(width=250, height=250)  # background_fill_color="# fafafa")
s2.triangle(x, y2, size=12, color="#c02942", alpha=0.8)

s3 = figure(width=250, height=250)  # background_fill_color="# fafafa")
s3.square(x, y3, size=12, color="#d95b43", alpha=0.8)

# COLUMN LAYOUT
# show(row(s1, s2, s3))

# grid layout
grid = gridplot([[s1, s2], [None, s3]], width=250, height=250)
gridplot([s1, s2, s3], ncols=2, merge_tools=False)

show(grid)
