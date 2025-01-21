# Load dash libraries
from dash import Input, Output, State

import dash_bootstrap_components as dbc

from dash_extensions.enrich import DashProxy, MultiplexerTransform

import secrets

# Load other python libraries
import os
import sys

# Load AIM_libraries
import dash_app_layout
import dash_app_viewmodel

# ## Set app
app = DashProxy(
    prevent_initial_callbacks='initial_duplicate',
    transforms=[MultiplexerTransform()],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    ) # = Dash()

app.layout = dash_app_layout.get_dash_app_layout_div()

app.secret_key = secrets.token_bytes(32)

# ## Set callbacks

# Dimension Reduction
@app.callback(
    Input(component_id={"index": "visualizeDimensionReductionN", "type": "visualizeDimensionReduction_specific"}, component_property='value'),
    Input(component_id={"index": "visualizeDimensionReductionColour", "type": "visualizeDimensionReduction_specific"}, component_property='value'),
    
    Output("dash-figure-loading", 'children'),
    )
def update_get_dimension_reduction_fig(
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour
    ):

    return dash_app_viewmodel.update_get_dimension_reduction_fig(**locals())


# ## Run app

# On local machine as main
if __name__ == '__main__':

    start_string = "\n=========== Dash ===========\n\n--> app.run_server() starts\n"

    print(start_string)

    app.run_server(debug=True, use_reloader=False)