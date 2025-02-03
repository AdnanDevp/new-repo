## Load the packages
import pandas as pd
import numpy as np

from sklearn.decomposition import TruncatedSVD, PCA

import plotly.express as plx

import copy
import os
import sys
import time

from functools import wraps

##
class Group_Data: 
    """Have all data grouping functionality combined in one class
    """
    # Available datasets from plotly.express
    available_datasets = {
        'iris': {'data': plx.data.iris, 'numeric_cols': ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']},
        'gapminder': {'data': plx.data.gapminder, 'numeric_cols': ['lifeExp', 'pop', 'gdpPercap']},
        'tips': {'data': plx.data.tips, 'numeric_cols': ['total_bill', 'tip']},
        'wind': {'data': plx.data.wind, 'numeric_cols': ['frequency', 'strength']},
        'carshare': {'data': plx.data.carshare, 'numeric_cols': ['car_hours', 'car_start_hour', 'car_end_hour']},
    }

    def __init__(self):
        self.current_dataset = 'iris'  # Default dataset

    def set_dataset(self, dataset_name):
        """Change the current dataset
        
        Args:
            dataset_name (str): Name of the dataset to use
        
        Returns:
            bool: True if dataset was successfully changed, False otherwise
        """
        if dataset_name in self.available_datasets:
            self.current_dataset = dataset_name
            return True
        return False

    def get_available_datasets(self):
        """Get list of available datasets
        
        Returns:
            list: Names of available datasets
        """
        return list(self.available_datasets.keys())

    ## Get dimension reduction data cloud
    def get_dimension_reduction(self, visualize_data):
        """Get dimension reduction for the current dataset
        
        Args:
            visualize_data (dict): Visualization parameters
        
        Returns:
            pandas.DataFrame: Reduced dimension data
        """
        # Get current dataset configuration
        dataset_config = self.available_datasets[self.current_dataset]
        
        # Load the dataset
        df = dataset_config['data']()
        
        # Select numeric columns for PCA
        X = df[dataset_config['numeric_cols']]
        
        # Perform PCA
        pca = PCA(n_components=visualize_data["visualizeDimensionReductionN"], random_state=17)
        X_plot = pd.DataFrame(pca.fit_transform(X), index=X.index)

        return X_plot
