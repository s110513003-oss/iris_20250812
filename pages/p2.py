import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title('IRIS品種預測')
# 載入模型
svm = joblib.load('models/svm.joblib')
rf = joblib.load('models/rf.joblib')
knn = joblib.load('models/knn.joblib')
LR = joblib.load('models/LR.joblib')

# 左側側邊欄：選擇模型
s1 = st.sidebar.selectbox('選擇模型', ['SVM','KNN', 'RandomForest', 'LogisticRegression'])
if s1 == 'SVM':
    model = svm
elif s1 == 'KNN':
    model = knn
elif s1 == 'RandomForest':
    model = rf
elif s1 == 'LogisticRegression':
    model = LR

st.image('iris.png')

# 接收使用者輸入：4個特徵
df = pd.read_csv('iris.csv')
se1 = st.slider('花萼長度(cm)', float(df['sepal.length'].min())-0.5, #最小
                float(df['sepal.length'].max())+0.8,  # 最大  #加float是怕數字被欄位名影響變str
                float(df['sepal.length'].mean())) # 預設值

se2 = st.slider('花萼寬度(cm)', float(df["sepal.width"].min())-0.5, #最小
                float(df["sepal.width"].max())+0.8,  # 最大  #加float是怕數字被欄位名影響變str
                float(df["sepal.width"].mean())) # 預設值

se3 = st.slider('花瓣長度(cm)', float(df['petal.length'].min())-0.5, #最小
                float(df['petal.length'].max())+0.8,  # 最大  #加float是怕數字被欄位名影響變str
                float(df['petal.length'].mean())) # 預設值

se4 = st.slider('花瓣寬度(cm)', float(df['petal.width'].min())-0.5, #最小
                float(df['petal.width'].max())+0.8,  # 最大  #加float是怕數字被欄位名影響變str
                float(df['petal.width'].mean())) # 預設值

labels = ['Setosa', 'Versicolor', 'Virginica']
if st.button('進行預測'):
    X = np.array([[se1,se2,se3,se4]])
    y = model.predict(X)
    st.write(f'### 預測結果：{y}')
    st.write(f'### 品種名稱：{labels[y[0]]}') # y是series 所以要看第一欄[0]才能找到