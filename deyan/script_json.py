from flask import Flask, request, jsonify, render_template, redirect
import json



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/vlad")
def helloVladi():
    return "Vladimir is rich!"

@app.route("/run_script")
def run_script():
    import sys
    import os
    import time

    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn import svm
    from sklearn.metrics import classification_report
    import matplotlib.pyplot as plt

    import pickle
    classifier_linear = pickle.load(open('classifier_linear.pk', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pk', 'rb'))

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
        qwe = zip(classifier_linear.classes_, priediction_proba[0]) #shows all propabilities
        asd = {k:v for k,v in qwe}
        asd['feeling'] = prediction_rbf
        print(asd)



        
    # # exit()
    # prediction_linear = classifier_linear.predict(test_vectors)
    # t2 = time.time()
    # time_linear_train = t1-t0
    # time_linear_predict = t2-t1

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

    # with open('result.json', 'w') as fp:
 #    json.dump(sample, fp)
        # print("Results for LinearSVC()")
        # print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
        # print(classification_report(test_labels, prediction_liblinear))


    
@app.route('/analyze', methods=['POST','GET'])
def analyze():
    if request.method == 'GET':
        return render_template('analyze_form.html')
    if request.method == 'POST':
        import sys
        import os
        import time

        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn import svm
        from sklearn.metrics import classification_report
        import matplotlib.pyplot as plt

        import pickle

        classifier_linear = pickle.load(open('classifier_linear.pk', 'rb'))
        vectorizer = pickle.load(open('vectorizer.pk', 'rb'))

        # Perform classification with SVM, kernel=rbf
        # classifier_rbf = svm.SVC()
        # t0 = time.time()
        # classifier_rbf.fit(train_vectors, train_labels)
        # t1 = time.time()

           


        # t2 = time.time()
        # time_rbf_train = t1-t0
        # time_rbf_predict = t2-t1

        # Perform classification with SVM, kernel=linear

        var = request.data
        print(request.data)
        our_test = vectorizer.transform([var])
        prediction_rbf = classifier_linear.predict(our_test)
        priediction_proba = classifier_linear.predict_proba(our_test)
        qwe = zip(classifier_linear.classes_, priediction_proba[0]) #shows all propabilities
        asd = {k:v for k,v in qwe}
        asd['feeling'] = prediction_rbf[0]
        print(prediction_rbf)
        print(type(prediction_rbf))
        return jsonify(**asd)
        # with open('result.json', 'w') as f:
        #   # for emotion in request.data.keys():
        #   #   result[emotion] = request.json[emotion]
        #   print(request)
        #   json.dumps(request.data, f)
        # return redirect("http://google.com")


# @app.route('/postMetho/<int:post_id>')
# def show_post(post_id):
#   methods = ['POST']
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


if __name__ == "__main__":
    app.run()