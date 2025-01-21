# ##
from dash import dcc, html, dash_table

import dash_bootstrap_components as dbc

# ##
import plotly.graph_objects as go

import sys
import os

from libraries.get_dimension_reduction import get_dimension_reduction_layout

# ##
def get_dash_app_layout_div():

    # current_user = dash_app_helper.get_current_user()

    layout = html.Div(

        children = [

            html.Div(
                id = 'dash_root',
                children=[
                    dcc.Loading(
                        children=[
                            get_dimension_reduction_layout(),
                        ],
                        type="default"
                    )
                ],
                
                style={
                    'display' : 'block',
                    'padding': 10,
                    "width" : "25%",
                    "height" : "100%",
                }
            ),

            html.Div(
                id = "dash_root_results",
                children=[
                    dcc.Loading(
                        id="dash-figure-loading",
                        children = [
                            dcc.Graph(
                                id={"index" : "figure_id", "type" : "dash_figure_go"}
                            )
                        ],
                        style={
                            'display': 'block', 
                            "position" : "fixed", 
                            "zIndex" : 1,
                            "width" : "70%",
                            "height" : "100%"
                        }
                    )
                ]
            )
        ],

        id="dash_app_layout_div",
        style={
            'display': 'flex',
            'flexDirection': 'row',
            'height': '95vh'
        }
    )

    return layout