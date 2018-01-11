from sklearn import svm
# higher value of C = more accurate
clf = svm.SVC(C=10000,kernel='rbf')
t0 = time()
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"
# calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
# predict value for 10th, 26th, 50th values (val either 1,0)
answer= pred[10] # 1
print answer
answer1 = pred[26] # 0
print answer1
answer2 = pred[50] # 1
print answer2
"""
for i in (pred):
    if pred[i] == 1:
        count = count + 1
print "count:", count
"""
print len(pred)
print accuracy

