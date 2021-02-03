# This simple example uses decision tree algorithm to predict based on a simple data

from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 1 is smooth and 0 is bumpy
labels = [0, 0, 1, 1] # 0 is apple and 1 is oranges

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

print (clf.predict([[150, 1 ]]))

