# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

### Description
For project 3, my goal is two-fold:
1. Using [Pushshift's](https://github.com/pushshift/api) API, you'll collect posts from two subreddits of your choosing.
2. Using NLP to train a classifier on which subreddit a given post came from. This is a binary classification problem.


---

### Requirements

- Gather and prepare your data using the `requests` library.
- **Create and compare two models**. One of these must be a Random Forest classifier, however the other can be a classifier of your choosing: logistic regression, KNN, SVM, etc.
- A Jupyter Notebook with your analysis for a peer audience of data scientists.
- An executive summary of your results.
- A short presentation outlining your process and findings for a semi-technical audience.

**Pro Tip:** You can find a good example executive summary [here](https://www.proposify.biz/blog/executive-summary).

## Project Workflow
![3](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Project%203.png)

- **Step 1** of the project: **Problem Statement and background**

- **[Step 2](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/01_API_Web_Scrabbing.ipynb)** of the project focuses on **Data wrangling/gathering/acquisition and cleansing**. Using [Pushshift's](https://github.com/pushshift/api) API to collect posts from two subreddits . (clean the data from unstructured/semi-structured sources and export to [csv file](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/reddit_clean.csv). 

- **[Step 3](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/02_NLP-EDA.ipynb)** of the project focuses on **Natural Language Processing and EDA**. Converting standard text data (like Titles and Comments) into a format that is available to be analyzed and fitted in modeling. Then export it to [csv file](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/data_nlp.csv). Some EDA chart from this step:
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/wd_ist.png)
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/wd_wsb.png)

- **Step 4** of the project focuses on **Classification Modeling**. There are two parts for model optimization. In the [first half](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/03_Model_Training.ipynb),  I fitted various models (**Random Forest classifier, logistic regression classifier, KNN, SVM**, etc) and use RandomizedSearchCV to find models with the best perfomance according to different metrics (**recall, accuracy, auc-roc, f1 score, f beta score**).
![](https://github.com/StevenZhangzhexu/DSIF-SG-7/blob/main/Project%203/images/Models.png)
