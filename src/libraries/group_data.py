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
    """Have all data grouping functionalities combined in one class
    """
    # Available datasets from plotly.express
    available_datasets = {
        'iris': ('sepal_length', 'sepal_width', 'petal_length', 'petal_width'),
        'tips': ('total_bill', 'tip', 'size'),
        'gapminder': ('gdpPercap', 'lifeExp', 'pop'),
        'wind': ('direction', 'strength', 'frequency'),
        'carshare': ('coord_x', 'coord_y', 'day', 'hour'),
        'stocks': ('GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT')
    }

    def __init__(self):
        """Initialize with default dataset"""
        self.current_dataset = 'iris'
        self._load_dataset()

    def _load_dataset(self):
        """Load the current dataset and prepare numeric columns"""
        dataset_loader = getattr(px.data, self.current_dataset)
        self.data = dataset_loader()
        
        # Get numeric columns for the current dataset
        self.numeric_columns = [col for col in self.available_datasets[self.current_dataset]]
        self.X = self.data[list(self.numeric_columns)]

    def set_dataset(self, dataset_name):
        """Change the current dataset
        
        Args:
            dataset_name (str): Name of the dataset from available_datasets
        """
        if dataset_name not in self.available_datasets:
            raise ValueError(f"Dataset {dataset_name} not found. Available datasets: {list(self.available_datasets.keys())}")
        
        self.current_dataset = dataset_name
        self._load_dataset()

    def get_dataset_info(self):
        """Get information about the current dataset
        
        Returns:
            dict: Dictionary containing dataset information
        """
        return {
            'name': self.current_dataset,
            'rows': len(self.data),
            'numeric_columns': self.numeric_columns,
            'all_columns': list(self.data.columns)
        }

    def get_available_datasets(self):
        """Get list of available datasets
        
        Returns:
            dict: Dictionary of available datasets and their numeric columns
        """
        return self.available_datasets

    ## Get dimension reduction data cloud
    def get_dimension_reduction(self, visualize_data):
        """Perform dimensionality reduction on the current dataset
        
        Args:
            visualize_data (dict): Dictionary containing visualization parameters
        
        Returns:
            pandas.DataFrame: Transformed data
        """
        pca = PCA(n_components=visualize_data["visualizeDimensionReductionN"], random_state=17)
        X_plot = pd.DataFrame(pca.fit_transform(self.X), index=self.X.index)

        return X_plot