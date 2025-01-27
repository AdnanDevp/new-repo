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
    # Define marker size options as a class attribute
    marker_size_options = [6, 8, 10, 12, 14]
    default_marker_size = 8

    ## Plot dimension reduction data cloud
    def get_dimension_reduction(self, X, visualize_data):
        
        marker_size = visualize_data.get("visualizeDimensionReductionMarkerSize", self.default_marker_size)
        
        if visualize_data["visualizeDimensionReductionN"] == 2:
            fig = go.Scatter(
                        x = X[0], 
                        y = X[1],
                        mode="markers",
                        marker_color=visualize_data["visualizeDimensionReductionColour"],
                        marker_size=marker_size
                    )

        elif visualize_data["visualizeDimensionReductionN"] == 3:
            # For 3D plots, we typically want slightly smaller markers
            marker_size_3d = max(2, marker_size // 2)  # Ensure minimum size of 2
            fig = go.Scatter3d(
                        x = X[0],
                        y = X[1],
                        z = X[2],
                        mode="markers",
                        marker_color=visualize_data["visualizeDimensionReductionColour"],
                        marker_size=marker_size_3d
                    )

        return go.Figure(fig)