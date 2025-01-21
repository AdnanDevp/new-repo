#
from contextvars import copy_context

from dash import dcc, html
from dash._callback_context import context_value
from dash._utils import AttributeDict
from dash.dash import no_update

import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import pytest

import plotly.graph_objects as go

import time
import os
import sys

#
import local_parameter

sys.path.append(os.path.join(os.path.abspath(local_parameter.current_project_folder), 'src'))
import dash_app


# Unit tests
@pytest.mark.parametrize(
    (
        "visualizeDimensionReductionN",
        "visualizeDimensionReductionColour"
    ),
    (
        pd.MultiIndex.from_product([
            [2,3],
            ["orange", "blue"]
        ])
        .to_frame()
    ).values
    )
def test_get_dimension_reduction_fig(
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour
    ):

    expected = {
        "visualizeDimensionReductionN" : type(go.Scatter()) if visualizeDimensionReductionN == 2 else type(go.Scatter3d()),
        "visualizeDimensionReductionColour" : visualizeDimensionReductionColour
    }

    def mock_callback():

        context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": """{"index": "visualizeDimensionReductionN", "type": "visualizeDimensionReduction_specific"}.value"""}]}))

        return dash_app.update_get_dimension_reduction_fig(**{
            "visualizeDimensionReductionN" : visualizeDimensionReductionN,
            "visualizeDimensionReductionColour" : visualizeDimensionReductionColour
            
        })

    ctx = copy_context()

    output = ctx.run(mock_callback)

    fig = output[0].figure

    actual = {
        "visualizeDimensionReductionN" : type(fig.data[0]),
        "visualizeDimensionReductionColour" : fig.data[0]["marker_color"]
    }

    assert expected == actual