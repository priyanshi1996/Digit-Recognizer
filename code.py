import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# The competition datafiles are in the directory ../input
# Read competition data files:
#image is of size 28*28
train = pd.read_csv("train.csv")
predict_data  = pd.read_csv("predict.csv")

# Write to the log:
print("Training set has {0[0]} rows and {0[1]} columns".format(train.shape))
print("Test set has {0[0]} rows and {0[1]} columns".format(predict_data.shape))
# Any files you write to the current directory get shown as outputs

train_Y = train.iloc[:35000,0]
train_X = train.iloc[:35000,1:]
test_Y=train.iloc[35000:,0]
test_X=train.iloc[35000:,1:]

#Random Forest Classifier

clf_random = RandomForestClassifier(n_estimators = 100,max_depth = 20,random_state = 0)
clf_random.fit(train_X,train_Y)
predicted_test_random=clf_random.predict(test_X)
print("Random Forest Classifier")
print(accuracy_score(test_Y,predicted_test_random))
#accuracy of random forest Classifier=0.96528

#Decision tree Classifier

clf_decision= DecisionTreeClassifier(criterion="entropy" , max_depth=7)
clf_decision.fit(train_X,train_Y)
predict_test_decision=clf_decision.predict(test_X)
print("Decision Tree")
print(accuracy_score(test_Y,predict_test_decision))
#accuracy of decision tree Classifier=0.79957142

#Naive Bayes

clf_bayes=MultinomialNB()
clf_bayes.fit(train_X,train_Y)
predict_test_bayes=clf_bayes.predict(test_X)
print("Naive Bayes")
print(accuracy_score(test_Y,predict_test_bayes))
#accuracy of naive bayes=0.8217142857

"""
#Support Vector Classifier

clf_svc=SVC(kernel="linear",gamma=0.001,C=1)
clf_svc.fit(train_X,train_Y)
predict_test_svc=clf_svc.predict(test_X)
print("Support Vector Classifier")
print(accuracy_score(test_Y,predict_test_svc))

Not at all recommended for this data set. Its too slow
"""
# As we can see that Random Forest Classifier is giving the best results 
# So we will use Random Forest Classifier to predict classes for our data

result = clf_random.predict(predict_data)
fp = open('digit-recognizer', 'a+')
fp.write('ImageId,Label\n')
for i,j in zip(range(len(result)), result):
    fp.write(str(i + 1))
    fp.write(',')
    fp.write(str(j))
    fp.write('\n')
fp.close()
print("File has been saved")
