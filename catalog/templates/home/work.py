from bokeh.plotting import figure, output_file, show

#make graph
def makegraph(x,y):
    output_file('showgraph.html')
    p = figure(
        title = 'Your graph',
        x_axis_label = 'X Axis',
        y_axis_label = 'Y axis'
        

    )
    p.line(x,y, legend='Test', line_width=2)

    #show results
    show(p)

