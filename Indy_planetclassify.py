import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from sklearn.model_selection import train_test_split #we don't use it here, but it's a useful function!
from sklearn.tree import DecisionTreeClassifier #how methods are imported
from sklearn import metrics #this will give us access to evaluation metrics


font = {'size'   : 20}
matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=20)
matplotlib.rc('ytick', labelsize=20)
matplotlib.rcParams['figure.dpi'] = 300

from io import StringIO
from IPython.display import Image
import pydotplus
from sklearn.tree import export_graphviz

LearningSet = pd.read_csv('HPLearningSet.csv')

LearningSet = LearningSet.drop(LearningSet.columns[0], axis=1) #We want to drop the first column of the file

LearningSet