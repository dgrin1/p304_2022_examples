import numpy as np

import matplotlib

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

import pandas as pd

from sklearn.model_selection import train_test_split  # we don't use it here, but it's a useful function!

from sklearn.tree import DecisionTreeClassifier  # how methods are imported

from sklearn import metrics  # this will give us access to evaluation metrics

font = {'size': 20}
matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=20)
matplotlib.rc('ytick', labelsize=20)
matplotlib.rcParams['figure.dpi'] = 300

# Here is a bunch of packages for visualization purposes only - this cell can be skipped if troublesome

from io import StringIO
from IPython.display import Image
import pydotplus
from sklearn.tree import export_graphviz

LearningSet = pd.read_csv('HPLearningSet.csv')

LearningSet = LearningSet.drop(LearningSet.columns[0], axis=1)  # We want to drop the first column of the file

TrainSet = LearningSet.iloc[:18, :]  # normally this would happen at random, using the function train_test_split

TestSet = LearningSet.iloc[18:, :]

Xtrain = TrainSet.drop(['P_NAME', 'P_HABITABLE'], axis=1)

Xtest = TestSet.drop(['P_NAME', 'P_HABITABLE'], axis=1)

ytrain = TrainSet.P_HABITABLE

ytest = TestSet.P_HABITABLE

model = DecisionTreeClassifier(
    random_state=3)  # This is how we specify which method we'd like to use, and any parameters.

model.fit(Xtrain, ytrain)  # This tiny line is how we build models in sklearn.

# dot_data = StringIO()
# export_graphviz(model, out_file=dot_data, feature_names=['Stellar Mass (M*)', 'Orbital Period (d)', 'Distance (AU)'], class_names=['Not Habitable', 'Habitable'], filled=True, rounded=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# nodes = graph.get_node_list()
#
# for node in nodes:
#     if node.get_label():
#         values = [int(ii) for ii in node.get_label().split('value = [')[1].split(']')[0].split(',')]
#         values = [255 * v / sum(values) for v in values]
#
#         values = [int(255 * v / sum(values)) for v in values]
#
#         if values[0] > values[1]:
#             alpha = int(values[0] - values[1])
#             alpha = '{:02x}'.format(alpha)  # turn into hexadecimal
#             color = '#20 B2 AA' + str(alpha)
#         else:
#             alpha = int(values[1] - values[0])
#             alpha = '{:02x}'.format(alpha)
#             color = '#FF 00 FF' + str(alpha)
#         node.set_fillcolor(color)
#
# graph.set_dpi('300')
#
# Image(graph.create_png())
#
# # Image(graph.write_png('Graph.png'))


from sklearn import tree

plt.figure(figsize=(2, 2))  # customize according to the size of your tree

tree.plot_tree(model, feature_names=['Stellar Mass (M*)', 'Orbital Period (d)', 'Distance (AU)'],
               class_names=['Not Habitable', 'Habitable'])

plt.show()

plt.figure(figsize=(12, 8))

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#20B2AA', '#FF00FF'])

# Will now plot the train set and test set points

plt.scatter(TrainSet['S_MASS'], TrainSet['P_PERIOD'], marker='*', \
            c=TrainSet['P_HABITABLE'], s=100, cmap=cmap, label='Train')

plt.scatter(TestSet['S_MASS'], TestSet['P_PERIOD'], marker='o', \
            c=TestSet['P_HABITABLE'], s=100, cmap=cmap, label='Test')

plt.yscale('log')

plt.xlabel('Mass of Parent Star (Solar Mass Units)')

plt.ylabel('Period of Orbit (days)');

# I can add the splits to the plot

plt.axvline(x=0.83, linewidth=1, ls='-', label='1st split', c='k')

plt.axhline(y=4.891, xmin=0, xmax=0.655, linewidth=1, ls='--', label='2nd split', c='k')

plt.text(0.845, 10 ** 3, '1st split', fontsize=14)

plt.text(0.65, 6, '2nd split', fontsize=14)

# Add legend, including unlabeled objects

bluepatch = mpatches.Patch(color='#20B2AA', label='Not Habitable')

magentapatch = mpatches.Patch(color='#FF00FF', label='Habitable')

plt.legend();

ax = plt.gca()
leg = ax.get_legend()
leg.legendHandles[2].set_color('k')
leg.legendHandles[3].set_color('k')

plt.legend(handles=[leg.legendHandles[2], leg.legendHandles[3], magentapatch, bluepatch], \
           loc='upper left', fontsize=14);
