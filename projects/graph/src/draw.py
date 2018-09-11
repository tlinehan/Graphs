"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
# from bokeh.palettes import Spectral8
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        # pass  # TODO
        self.graph = graph

        N = len(graph.vertices)

        node_indices = list(graph.vertices)

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
                       tools='', toolbar_location=None)

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

        ### start of layout code
        circ = [int(v) for v in graph.vertices]
        x = [2 * (i // 3) for i in circ]
        y = [2 * (i % 3) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        output_file('graph.html')
        show(plot)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# below creates error
# graph.add_edge('0', '4')
print(graph.vertices)


my_graph = BokehGraph()
