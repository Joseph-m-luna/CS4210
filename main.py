#-------------------------------------------------------------------------
# AUTHOR: Joseph Luna
# FILENAME: main.py
# SPECIFICATION: Decision Tree ML code
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
mappings = []
for x in range(len(db[0])):
    mappings.append(dict())
counter = 1
for row in db:
    index = 1
    newObj = []
    for item in row[:-1]:
        if item in mappings[index-1]:
            newObj.append(mappings[index-1][item])
        else:
            mappings[index-1][item] = len(mappings[index-1]) + 1
            newObj.append(mappings[index-1][item])
            counter += 1
        index += 1
    X.append(newObj)
print(X)
# X = [[1, 1, 1, 1], [2, 1, 1, 2], [3, 1, 1, 1], [3, 1, 1, 2], [2, 1, 2, 2], [1, 1, 2, 2], [1, 2, 1, 1], [3, 1, 2, 1], [2, 2, 1, 1], [1, 1, 2, 1]]

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
labels = dict()
counter = 1
for row in db:
    print(row)
    item = row[-1]
    print(item)

    if item in labels:
        Y.append(labels[item])
    else:
        labels[item] = counter
        Y.append(labels[item])
        counter += 1
print(Y)

# Y =

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()