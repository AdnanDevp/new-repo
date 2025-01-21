# Load dash libraries
from dash import dcc, html, Input, Output, State, ctx, dash_table
from dash.dash import no_update

import dash_bootstrap_components as dbc

from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, MultiplexerTransform

from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

import flask

import base64
import secrets

# Load other python libraries
import copy
from functools import wraps
import logging
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random

import uuid

import os
import re
import sys
import time
import json
import shutil

from libraries.get_dimension_reduction import get_dimension_reduction_items, update_get_dimension_reduction_fig_layout
from libraries.group_data import Group_Data
from libraries.visualize_data import Visualize_Data

# ##
def update_get_dimension_reduction_fig(
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour,
        visualizeDimensionReductionMarkerSize
    ):

    if (ctx.triggered_id 
        and bool(visualizeDimensionReductionN)
        and bool(visualizeDimensionReductionColour)
        and bool(visualizeDimensionReductionMarkerSize)):

        visualize_data = get_dimension_reduction_items(
            visualizeDimensionReductionN,
            visualizeDimensionReductionColour,
            visualizeDimensionReductionMarkerSize
        )

        X_plot = Group_Data().get_dimension_reduction(visualize_data)

        fig = Visualize_Data().get_dimension_reduction(X_plot, visualize_data)
        fig = update_get_dimension_reduction_fig_layout(fig, visualize_data)
        
        return [
            dcc.Graph(
                figure=fig,
                id={"index" : "figure_id", "type" : "dash_figure_go"}
            )
        ]

    else:
        raise PreventUpdate