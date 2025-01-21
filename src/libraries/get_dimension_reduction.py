from dash import html, dcc

# ##
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
                ]
            ),

        ], 
        id={"index": "visualizeDimensionReduction", "type": "dash_app_layout_page"},
    )

    return layout

def get_dimension_reduction_items(
        visualizeDimensionReductionN,
        visualizeDimensionReductionColour
    ):

    visualize_data = dict()

    visualize_data['visualizeDimensionReductionN'] = visualizeDimensionReductionN

    visualize_data['visualizeDimensionReductionColour'] = visualizeDimensionReductionColour

    return visualize_data    

def update_get_dimension_reduction_fig_layout(fig, visualize_data):
    
    title_string = f"{visualize_data['visualizeDimensionReductionN']}-Dimension Reduction plotly.express.data.iris()"

    fig.update_layout(title_text=title_string)

    return fig