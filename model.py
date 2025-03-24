import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

#read csv file
df = pd.read_csv("Campus_Selection.csv")

#drop unwanted column
df.drop(columns=['sl_no'],inplace=True)

#preprocess data
le = LabelEncoder()
df['status'] = le.fit_transform(df['status'])

categorical_columns = ['gender','ssc_b','hsc_b','hsc_s','degree_t','workex','specialisation']
numerical_columns = ['ssc_p','hsc_p','degree_p','etest_p','mba_p']

ct = ColumnTransformer(transformers=[
                       ("cat",OneHotEncoder(),categorical_columns),
                        ("num",StandardScaler(),numerical_columns)])


#Split data into independent and dependent variables
x = df.iloc[:,:-1]
y =df['status']

x_transformed = ct.fit_transform(x)

#Split into train and test split
x_train,x_test,y_train,y_test = train_test_split(x_transformed,y,test_size=0.25,random_state=1)

'''
#Train different algorthims to find suitable one
pipelines = {
    'lr': make_pipeline(LogisticRegression()),
    'dt':make_pipeline(DecisionTreeClassifier()),
    'rf':make_pipeline(RandomForestClassifier()),
    'NB':make_pipeline(GaussianNB()),
    'knn':make_pipeline(KNeighborsClassifier())

}

for model_name,model_pipelines in pipelines.items():
    model_pipelines.fit(x_train,y_train)

    y_pred = model_pipelines.predict(x_test)

    acc = accuracy_score(y_test,y_pred)

    print(f"{model_name} and its accuracy {acc}")

'''

lr = LogisticRegression()

lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)


#Save the model as a pickle file
with open("model.pkl",'wb')as f:
    pickle.dump(lr,f)

#Save the column transformer as a pickle file
with open("columntransformer.pkl",'wb')as pf:
    pickle.dump(ct,pf)

#Save the label encoder as a pickle file
with open("labelencoder.pkl",'wb') as lf:
    pickle.dump(le,lf)