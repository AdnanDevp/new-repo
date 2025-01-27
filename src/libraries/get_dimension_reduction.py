from dash import html, dcc
from .visualize_data import Visualize_Data

def get_dimension_reduction_layout():
    layout = html.Div(
        children=[
            html.H4("Having a dimension reduction"),
            html.Div(" > plotly.express.data.iris() < "),

            html.Br(),

            html.Div(
                children = [
                    html.Div(
                        children = [
                            "Dimension",
                        ]
                    ),
                    dcc.Dropdown(
                        [1, 2, 3],  # Added 1D option
                        id={"index": "visualizeDimensionReductionN", "type": "visualizeDimensionReduction_specific"},
                    ),
                    html.Br(),

                    html.Div(
                        children = [
                            "Colour",
                        ]
                    ),
                    dcc.Dropdown(
                        ["green", "red", "purple"],
                        id={"index": "visualizeDimensionReductionColour", "type": "visualizeDimensionReduction_specific"},
                    ),
                    html.Br(),

                    html.Div(
                        children = [
                            "Marker Size",
                        ]
                    ),
                    dcc.Dropdown(
                        Visualize_Data.marker_size_options,
                        value=Visualize_Data.default_marker_size,
                        id={"index": "visualizeDimensionReductionMarkerSize", "type": "visualizeDimensionReduction_specific"},
                    ),
                    html.Br(),
                ]
            ),

        ], 
        id={"index": "visualizeDimensionReduction", "type": "dash_app_layout_page"},
    )

    return layout

def get_dimension_reduction_items(
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour,
        visualizeDimensionReductionMarkerSize
    ):

    visualize_data = dict()

    visualize_data['visualizeDimensionReductionN'] = visualizeDimensionReductionN
    visualize_data['visualizeDimensionReductionColour'] = visualizeDimensionReductionColour
    visualize_data['visualizeDimensionReductionMarkerSize'] = visualizeDimensionReductionMarkerSize

    return visualize_data    

def update_get_dimension_reduction_fig_layout(fig, visualize_data):
    
    title_string = f"{visualize_data['visualizeDimensionReductionN']}-Dimension Reduction plotly.express.data.iris()"

    fig.update_layout(title_text=title_string)
    
    # Update marker size for all traces in the figure
    for trace in fig.data:
        trace.marker.size = visualize_data['visualizeDimensionReductionMarkerSize']

    return fig