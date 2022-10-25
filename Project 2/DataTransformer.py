import numpy as np 
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin

# Calculate years since contstruction, remodel till sold
def f(a,b,c):
    return [c-a, c-b]


# Adder Transformer : To add year calculation
class columnAdderTransformer(BaseEstimator, TransformerMixin):  
    def fit(self, X , y=None):
        return self
    
    def transform(self, X,y=None):
        temp_cols = X.columns.to_list()
        temp_cols.extend(['Years of Construction','Years of Remodel'])
        new_cols = {k:v for k,v in zip(range(len(temp_cols)),temp_cols)}      
        years = X.apply(lambda x: f(x['Year Built'],x['Year Remod/Add'],x['Yr Sold']), axis=1) 
        # years is a col of list
        # split 1 column of list values to 2 columns 
        combined_df = pd.DataFrame(np.c_[years])
        combined_df[['y1','y2']] = pd.DataFrame(combined_df[0].tolist(), index= combined_df.index)
        years_col = combined_df[['y1','y2']]
        # append to X
        X_add = pd.DataFrame(np.c_[X,years_col]).rename(columns=new_cols)
        return X_add

# Dropper Transformer 
class columnDropperTransformer():
    def __init__(self,columns):
        self.columns=columns
    def transform(self,X,y=None):
        return X.drop(self.columns,axis=1)
    def fit(self, X, y=None):
        return self 
