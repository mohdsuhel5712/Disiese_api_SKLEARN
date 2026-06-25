import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
import pickle
# load data
data = pd.read_csv('data.csv')
# feature
x = data[['fever','cough','headache','fatigue']]
# target
y = data['disease']

# make obejct
model = DecisionTreeClassifier()
model.fit(x,y)
# use pickle
pickle.dump(model,open('model.pkl','wb'))
print('model train and saved')
