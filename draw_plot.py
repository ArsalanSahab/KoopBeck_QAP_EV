#### IMPORTS ####

import plotly as py # Python Plotting Library
import plotly.graph_objs as go

class PlotDrawer:

    @staticmethod
    def drawPlot(plot_name, generations, average_results, max_results, min_results):

        generations_rev = generations[::-1]
        min_results = min_results[::-1]

        # GRAPH SETTINGS

        max_and_min_trace = go.Scatter(
            x=generations + generations_rev,
            y=max_results + min_results,
            fill='tozerox',
            fillcolor='rgba(0,100,80,0.2)',
            line=go.scatter.Line(color='rgb(255,0,0,0)'),
            showlegend=True,
            name='Max and min',
        )

        average_trace = go.Scatter(
            x=generations,
            y=average_results,
            line=go.scatter.Line(color='rgb(0,100,80)'),
            mode='lines',
            name='Average',
        )

        data = [max_and_min_trace, average_trace]

        layout = go.Layout(
            title=plot_name,
            paper_bgcolor='rgb(255,255,255)',
            plot_bgcolor='rgb(229,229,229)',
            xaxis=go.layout.XAxis(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
            yaxis=go.layout.YAxis(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
        )

        ## SETTINGS END

        # CREATE GRAPH_FILE OFFLINE
        fig = go.Figure(data=data, layout=layout)
        py.offline.plot(fig, filename='plot_' + plot_name + '.html')
