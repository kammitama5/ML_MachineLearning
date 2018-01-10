from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)
return clf.fit(features_train, labels_train)


### create classifier
clf = GaussianNB()
### fit the classifier on the training features and labels
clf.fit(features_train, labels_train)
### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
return accuracy