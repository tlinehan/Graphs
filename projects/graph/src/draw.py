"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer, 
    StaticLayoutProvider, 
    Circle, 
    ColumnDataSource, 
    Label, 
    LabelSet
)
# from bokeh.palettes import Spectral8
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        # pass  # TODO
        self.graph = graph

        N = len(graph.vertices)

        node_indices = list(graph.vertices)

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1),
                       y_range=(-1.1,10.1), tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(['blue'] * N, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in graph.vertices:
            for edge_end in graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end) 

        graph_renderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)


"""
        ### start of layout code
        grid = [int(v) for v in graph.vertices]
        x = [2 * (i // 3) for i in grid]
        y = [2 * (i % 3) for i in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                        text_align='center',
                        text_baseline='middle',
                        text_color='white',
                        source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)

        print(graph.vertices)
"""

"""uncomment below to run part 1"""
# graph_part1 = Graph()  # Instantiate your graph
# graph_part1.add_vertex('0')
# graph_part1.add_vertex('1')
# graph_part1.add_vertex('2')
# graph_part1.add_vertex('3')
# graph_part1.add_edge('0', '1')
# graph_part1.add_edge('0', '3')
# # below creates tests error handling
# # graph_part1.add_edge('0', '4')
# print(graph_part1.vertices)
#
# BokehGraph(graph_part1)
""""end"""
# """part 4 data"""
#"""
graph_part4 = Graph()
graph_part4.add_vertex('0')
graph_part4.add_vertex('1')
graph_part4.add_vertex('2')
graph_part4.add_vertex('3')
graph_part4.add_vertex('4')
graph_part4.add_vertex('5')
graph_part4.add_vertex('6')
graph_part4.add_vertex('7')
graph_part4.add_vertex('8')
graph_part4.add_vertex('10')

graph_part4.add_edge('0', '1')
graph_part4.add_edge('0', '3')
graph_part4.add_edge('0', '4')
graph_part4.add_edge('3', '6')
graph_part4.add_edge('4', '5')
graph_part4.add_edge('4', '7')
graph_part4.add_edge('4', '8')
graph_part4.add_edge('5', '2')

# BokehGraph(graph_part4)
# graph_part4.depth_tranversal()
print(graph_part4.vertices)

#"""
