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
    # Available datasets and their numeric columns
    available_datasets = {
        'iris': {'data': px.data.iris, 'numeric_cols': ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']},
        'tips': {'data': px.data.tips, 'numeric_cols': ['total_bill', 'tip', 'size']},
        'gapminder': {'data': px.data.gapminder, 'numeric_cols': ['lifeExp', 'pop', 'gdpPercap']},
        'wind': {'data': px.data.wind, 'numeric_cols': ['direction', 'strength']},
        'stocks': {'data': px.data.stocks, 'numeric_cols': ['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT']}
    }

    ## Get dimension reduction data cloud
    def get_dimension_reduction(self, visualize_data):
        # Get the selected dataset
        dataset_name = visualize_data.get("selectedDataset", "iris")
        dataset_info = self.available_datasets[dataset_name]
        
        # Load the dataset
        df = dataset_info['data']()
        
        # Get numeric columns for the selected dataset
        X = df[dataset_info['numeric_cols']]

        # Perform PCA
        pca = PCA(n_components=visualize_data["visualizeDimensionReductionN"], random_state=17)
        X_plot = pd.DataFrame(pca.fit_transform(X), index=X.index)

        return X_plot

    @classmethod
    def get_available_datasets(cls):
        """Return list of available dataset names"""
        return list(cls.available_datasets.keys())