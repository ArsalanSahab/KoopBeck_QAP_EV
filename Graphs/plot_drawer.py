#### IMPORTS ####

import plotly as py # Python Plotting Library
import plotly.graph_objs as go

class PlotDrawer:

    @staticmethod
    def drawPlot(plot_name, generations, average_results, max_results, min_results, path):

        generations_rev = generations[::-1]
        min_results = min_results[::-1]

        # GRAPH SETTINGS

        # The trace for max and min
        # The y-values are taken from the result arrays
        # For the x-values, the generations list is compounded
        # with its reverse
        max_and_min_trace = go.Scatter(
            x = generations + generations_rev,
            y = max_results + min_results,
            fill = 'tozerox',
            fillcolor = 'rgba(0,100,80,0.2)',
            line = go.scatter.Line(color='rgb(255,0,0,0)'),
            showlegend = True,
            name = 'Maximum and Minimum Scores',
        )

        # The trace for the average results
        # Simple line that takes the generations list as x-axis
        # and average_results list as y-axis
        average_trace = go.Scatter(
            x = generations,
            y = average_results,
            line = go.scatter.Line(color='rgb(0,100,80)'),
            mode = 'lines',
            name = 'Average Score',
        )

        # Data used for the figure
        # A list consisting of all the traces to be drawn
        data = [max_and_min_trace, average_trace]

        # The graph_objs layout object used for the plot
        layout = go.Layout(
            title = plot_name,
            paper_bgcolor = 'rgb(255,255,255)',
            plot_bgcolor = 'rgb(229,229,229)',
            xaxis = go.layout.XAxis(
                gridcolor = 'rgb(255,255,255)',
                showgrid = True,
                showline = False,
                showticklabels = True,
                tickcolor = 'rgb(127,127,127)',
                ticks = 'outside',
                zeroline = False
            ),
            yaxis = go.layout.YAxis(
                gridcolor = 'rgb(255,255,255)',
                showgrid = True,
                showline = False,
                showticklabels = True,
                tickcolor = 'rgb(127,127,127)',
                ticks = 'outside',
                zeroline = False
            )
        )

        # Generate a plot (graph) and save it as an html file
        fig = go.Figure(data=data, layout=layout)
        py.offline.plot(fig, filename=path + '/' + plot_name + '.html')
