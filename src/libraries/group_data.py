## Load the packages
import pandas as pd
import numpy as np

from sklearn.decomposition import TruncatedSVD, PCA

import plotly.express as px

import copy
import os
import sys
import time

from functools import wraps

##
class Group_Data: 
    """Have all data grouping shizzle combined in one class
    """
    # Available datasets from plotly.express
    available_datasets = {
        "iris": {"func": px.data.iris, "numeric_cols": ["sepal_length", "sepal_width", "petal_length", "petal_width"]},
        "gapminder": {"func": px.data.gapminder, "numeric_cols": ["lifeExp", "pop", "gdpPercap"]},
        "tips": {"func": px.data.tips, "numeric_cols": ["total_bill", "tip", "size"]},
        "wines": {"func": px.data.wine, "numeric_cols": ["alcohol", "malic_acid", "ash", "alcalinity_of_ash", "magnesium", 
                                                      "total_phenols", "flavanoids", "nonflavanoid_phenols", "proanthocyanins", 
                                                      "color_intensity", "hue", "od280/od315_of_diluted_wines", "proline"]}
    }

    ## Get dimension reduction data cloud
    def get_dimension_reduction(self, visualize_data):
        # Get the selected dataset
        dataset_name = visualize_data.get("selectedDataset", "iris")
        dataset_info = self.available_datasets[dataset_name]
        
        # Load the dataset
        df = dataset_info["func"]()
        
        # Select numeric columns for PCA
        X = df[dataset_info["numeric_cols"]]

        pca = PCA(n_components=visualize_data["visualizeDimensionReductionN"], random_state=17)

        X_plot = pd.DataFrame(pca.fit_transform(X), index=X.index)

        return X_plot
