# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Classification Model using Web APIs & NLP to calssify reddit posts 

### Background And Problem Statement
As a part of marketing division of a fiancial company, I would like to efficiently advertise our different products AD on relevant subreddit. (e.g. less risky prodct for risk-adverse investor and more risky product for activist investor. Thus I choose the two bigeest subreddits relevant to investing, which are r/investing no r/Wallstreetbets. I will create a model to do binary text classification  based on the post to distinguish two subreddits.

![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/WallStreetBets-600x472.png)
**VS**
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/communityIcon_rfponci4qog61.png)

![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Screenshot%202022-11-04%20at%202.48.38%20AM.png)



## Project Workflow
![3](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Project%203.png)

- **Step 1** of the project: **Problem Statement and background**

- **[Step 2](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/01_API_Web_Scrabbing.ipynb)** of the project focuses on **Data wrangling/gathering/acquisition and cleansing**. Using [Pushshift's](https://github.com/pushshift/api) API to collect posts from two subreddits . (clean the data from unstructured/semi-structured sources and export to [csv file](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/reddit_clean.csv). 

- **[Step 3](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/02_NLP-EDA.ipynb)** of the project focuses on **Natural Language Processing and EDA**. Converting standard text data (like Titles and Comments) into a format that is available to be analyzed and fitted in modeling. Then export it to [csv file](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/data_nlp.csv). Some EDA chart from this step:
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/wd_ist.png)
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/wd_wsb.png)


- **Step 4** of the project focuses on **Classification Modeling**. There are two parts for model optimization. In the [first half](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/03_Model_Training.ipynb),  I fitted various models (**Random Forest classifier, logistic regression classifier, KNN, SVM**, etc) and use RandomizedSearchCV to find models with the best perfomance according to different metrics (**recall, accuracy, auc-roc, f1 score, f beta score**).
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Models.png)

After training various classification modles based on different vectorizers, I find the list of models with best perfomance as below:


| Vectorizer |stop_words | ngram_range  |  min_df | max_features  |  max_df | Model| penalty | C 
|---|---|---|---|---|---|---|---|---|
| CountVectorizer |english |  (1, 2) | 2  |  3500 | 0.5  |  RandomForestClassifier(max_depth=20, n_estimators=100)| NaN|NaN |
| TfidfVectorizer/CountVectorizer |english |  (1, 1) | 2  |  3500 | 0.7  | RandomForestClassifier(max_depth=20, n_estimators=50)| NaN|NaN |
| TfidfVectorizer |english |  (1, 1)|  1 |  2000 |  0.7 | LogisticRegression(C=0.1, solver='saga')|	L2|  0.1|
| TfidfVectorizer/CountVectorizer |english |  (1, 2)|  2 |  3000 |  0.7 | GradientBoostingClassifier(max_depth=20, n_estimators=250)|NaN|NaN |

In the [second half](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/04_Esemble_%20Model.ipynb), I combine the final models together to ensemble models to improve the accuracy and reduce variance.
* voting
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/vt.png)

* Boosing
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/ensMd2.png)

* Stacking
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Screenshot%202022-11-24%20at%201.25.04%20AM.png)


- **[Step 5] ConClusion : Aftter comapring a few ensemble models, we found that the stacking model and voting model has the same accuracy but AUC of stacking model is 0.91 which is higher than 0.90 of voting.
AUC - ROC curve is a performance measurement for the classification problems at various threshold settings. ROC is a probability curve and AUC represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes. Higher the AUC, the better the model is at predicting 0 classes as 0 and 1 classes as 1. Thus by analogy, the stacking model is the better the model at distinguishing between posts with the r/investing no r/Wallstreetbets .

**Reconmmendation**: We will use the final model (stacking) on our advertising proposal of different products to see if the result is correct. (if the advertising proposal for higher risk prodct goes to r/Wallstreetbets and lower risk to r/investing). If not, then adjusting our advertising proposal to correct the result for a better and more efficient advertising.
