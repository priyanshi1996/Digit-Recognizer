**# Digit-Recognizer using Python 3.6**

## Libraries Used are:-
1. sklearn
2. pandas

Here we have a file named "train.rar" which consists data of images of size 28 * 28.
Total no of images are 42000.
So we have a total of 42000 rows and (784+1) columns. Extra 1 is for levels of images (i.e. 1 to 9).

Starting 35000 images data is used for train the classifer and then that classifer is used to predict the labels of rest 7000 images and then those predicted lebels are compared to the actual data to calculate accuracy score.

## Classifier Used are
1. Random Forest Classifier
2. Decision Tree Classifier
3. Naive Bayes Classifier

## Accuracy score of above classifier are:-
1. Random Forest Classifier :- 0.94285714
2. Decision Tree Classifier :- 0.79957142
3. Naive Bayes Classifier :- 0.8217142857

So now as we can see that Random Forest Classifier gives us the best accuracy score, therefore it is used to predict the labels of images stored in file "predict.rar". Labels of predict.rar file will be stored in a file named "digit-recognizer".

## Instructions:- 
Download all the files and store them in a single folder and then run 'code.py' file.

