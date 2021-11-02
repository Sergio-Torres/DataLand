from bokeh.plotting import figure, output_file, show

x = [1,2,4,6,7]
y = [4,2,6,4,6]

output_file('graph1.html')

#add plot
p = figure(
    title = 'Example',
    x_axis_label = 'X Axis',
    y_axis_label = 'Y Axis'
)

#Render glyph
p.line(x,y, legend='Test', line_width=2)

#show results
show(p)