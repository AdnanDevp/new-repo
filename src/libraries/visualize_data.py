## Load the packages
import pandas as pd
import numpy as np

import plotly.express as plx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import matplotlib, matplotlib_venn

from functools import wraps

##
class Visualize_Data:
    """Have all data visualizing shizzle combined in one class
    """

    ## Plot dimension reduction data cloud
    def get_dimension_reduction(self, X, visualize_data):
        
        if visualize_data["visualizeDimensionReductionN"] == 2:

            fig = go.Scatter(
                        x = X[0], 
                        y = X[1],
                        mode="markers",
                        marker_color=visualize_data["visualizeDimensionReductionColour"],
                        marker_size=14
                    )

        elif visualize_data["visualizeDimensionReductionN"] == 3:
              
            fig = go.Scatter3d(
                        x = X[0],
                        y = X[1],
                        z = X[2],
                        mode="markers",
                        marker_color=visualize_data["visualizeDimensionReductionColour"],
                        marker_size=4
                    )

        return go.Figure(fig)