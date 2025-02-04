from dash import html, dcc
from .visualize_data import Visualize_Data
from .group_data import Group_Data

def get_dimension_reduction_layout():
    layout = html.Div(
        children=[
            html.H4("Having a dimension reduction"),

            html.Div(
                children = [
                    html.Div(
                        children = [
                            "Dataset",
                        ]
                    ),
                    dcc.Dropdown(
                        list(Group_Data.available_datasets.keys()),
                        value="iris",  # Default dataset
                        id={"index": "selectedDataset", "type": "visualizeDimensionReduction_specific"},
                    ),
                    html.Br(),

                    html.Div(
                        children = [
                            "Dimension",
                        ]
                    ),
                    dcc.Dropdown(
                        [2,3],
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
                        value=Visualize_Data.default_marker_size,  # Default value
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
        selectedDataset,
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour,
        visualizeDimensionReductionMarkerSize
    ):

    visualize_data = dict()

    visualize_data['selectedDataset'] = selectedDataset
    visualize_data['visualizeDimensionReductionN'] = visualizeDimensionReductionN
    visualize_data['visualizeDimensionReductionColour'] = visualizeDimensionReductionColour
    visualize_data['visualizeDimensionReductionMarkerSize'] = visualizeDimensionReductionMarkerSize

    return visualize_data    

def update_get_dimension_reduction_fig_layout(fig, visualize_data):
    
    title_string = f"{visualize_data['visualizeDimensionReductionN']}-Dimension Reduction of {visualize_data['selectedDataset']} dataset"

    fig.update_layout(title_text=title_string)
    
    # Update marker size for all traces in the figure
    for trace in fig.data:
        trace.marker.size = visualize_data['visualizeDimensionReductionMarkerSize']

    return fig