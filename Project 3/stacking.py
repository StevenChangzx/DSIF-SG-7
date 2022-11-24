import numpy as np 
import pandas as pd 
import copy as cp
from icecream import ic
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin

def copy_data(data_in):
    data_out = cp.deepcopy(data_in)
    try:
        data_out.reset_index(drop=True, inplace=True)
    except:
        pass
    return data_out

class Level1Stacker(BaseEstimator, TransformerMixin):
    
    def __init__(self, level_1_classifiers : dict, stack_method : str = "predict_proba", passthrough : bool = False, save_x : bool=False): # no *args or **kargs
        ic("Level1Stacker.init")
        self.level_1_classifiers = level_1_classifiers
        self.stack_method = stack_method
        self.passthrough = passthrough
        self.save_x = save_x

        self.X = None

    def fit(self, X, y=None):
        ic("Level1Stacker.fit")
        X_copy = copy_data(X) 

        for classifier in self.level_1_classifiers.values():
            classifier.fit(X_copy, y)

        return self

    def transform(self, X):
        ic("Level1Stacker.transform")
        X_copy = copy_data(X) 

        all_predictions = [None] * len(self.level_1_classifiers)

        for i, classifier in enumerate(self.level_1_classifiers.values()):
            if self.stack_method == "predict_proba":
                all_predictions[i] = classifier.predict_proba(X_copy)[:, 1]
            else:
                all_predictions[i] = classifier.predict(X_copy)

        df_stacking = pd.DataFrame(np.array(all_predictions).T, columns=[f"{name}_prediction" for name in self.level_1_classifiers.keys()])

        X_copy = pd.concat([df_stacking, X_copy], axis=1) if self.passthrough == True else df_stacking

        self.X = copy_data(X_copy) if self.save_x == True else None

        return X_copy
    
class Level2Stacker(BaseEstimator, ClassifierMixin):

    def __init__(self, model):
        ic("Level2Stacker.init")
        self.model = model

    def fit(self, X, y):
        ic("Level2Stacker.fit")
        self.model.fit(X, y)
        return self

    def predict(self, X):
        ic("Level2Stacker.predict")
        return self.model.predict(X)
    
    def predict_proba(self, X):
        ic("Level2Stacker.predict_proba")
        return self.model.predict_proba(X)
    
    @property
    def classes_(self):
        return self.model.classes_