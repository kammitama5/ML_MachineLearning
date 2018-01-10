### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
## time code
t0 = time()
### fit the classifier on the training features and labels
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
# time code predict
t1 = time()
### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"
### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy