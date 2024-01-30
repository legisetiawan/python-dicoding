import sklearn
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import cross_val_score
# Secara umum jika hasil dari pengujian tiap fold pada cross validation memiliki nilai yang bervariasi dari 0.85 sampai 0.99, maka model tersebut dapat dikatakan baik.
# Google lab

# Load iris dataset
iris = datasets.load_iris()

# mendefinisikan atribut dan label pada dataset
x=iris.data
y=iris.target

 
# membuat model dengan decision tree classifier
clf = tree.DecisionTreeClassifier()


 
# mengevaluasi performa model dengan cross_val_score
scores = cross_val_score(clf, x, y, cv=5)