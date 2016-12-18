import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

import pickle
classifier_linear = pickle.load(open('classifier_linear_POS_OR_NEG.pk', 'rb'))
vectorizer = pickle.load(open('vectorizerPOSITIVE_NEGATIVE.pk', 'rb'))

# Perform classification with SVM, kernel=rbf
# classifier_rbf = svm.SVC()
# t0 = time.time()
# classifier_rbf.fit(train_vectors, train_labels)
# t1 = time.time()

   


# t2 = time.time()
# time_rbf_train = t1-t0
# time_rbf_predict = t2-t1

# Perform classification with SVM, kernel=linear

while True:
    var = raw_input("Please enter something: ")
    our_test = vectorizer.transform([var])
    prediction_rbf = classifier_linear.predict(our_test)
    priediction_proba = classifier_linear.predict_proba(our_test)
    print(zip(classifier_linear.classes_, priediction_proba[0])) #shows all propabilities
    print(prediction_rbf) #shows determined label

    
# exit()
prediction_linear = classifier_linear.predict(test_vectors)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1

    # Perform classification with SVM, kernel=linear
    # classifier_liblinear = svm.LinearSVC()
    # t0 = time.time()
    # classifier_liblinear.fit(train_vectors, train_labels)
    # t1 = time.time()
    # prediction_liblinear = classifier_liblinear.predict(test_vectors)
    # t2 = time.time()
    # time_liblinear_train = t1-t0
    # time_liblinear_predict = t2-t1

    # Print results in a nice table
    # print("Results for SVC(kernel=rbf)")
    # print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    # print(classification_report(test_labels, prediction_rbf))
print("Results for SVC(kernel=linear)")
print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
print(classification_report(test_labels, prediction_linear))
    # print("Results for LinearSVC()")
    # print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    # print(classification_report(test_labels, prediction_liblinear))