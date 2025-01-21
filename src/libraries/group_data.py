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
    """Have all data grouping shizzle combined in one class
    """
    ## Get dimension reduction data cloud
    def get_dimension_reduction(self, visualize_data):

        X = plx.data.iris().iloc[:, :4]

        pca = PCA(n_components=visualize_data["visualizeDimensionReductionN"], random_state=17)

        X_plot = pd.DataFrame(pca.fit_transform(X), index=X.index)

        return X_plot
