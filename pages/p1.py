import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('IRIS相關資訊')
df = pd.read_csv('iris.csv')
st.write(df.head())

st.write('### 樣本散佈圖')


mapping = {'Setosa':0, 'Versicolor':1, 'Virginica':2}
colors = ['red', 'green', 'blue']
# 依照tab顯示不同欄位(分頁標籤)的分佈情形
tab1, tab2 = st.tabs(['依 花 萼 的 長 寬', '依 花 瓣 的 長 寬']) # 預設字體很小，想辦法增加長度
fig, ax = plt.subplots()
with tab1:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax.scatter(subset['sepal.length'], subset['sepal.width'], label=i, c=colors[s])
    ax.set_xlabel('sepal.length') #橫軸名稱
    ax.set_ylabel('sepal.width') #縱軸名稱  
    ax.legend()  #顯示圖例
    st.pyplot(fig)

fig2, ax2 = plt.subplots()
with tab2:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax2.scatter(subset['petal.length'], subset['petal.width'], label=i, c=colors[s])
    ax2.set_xlabel('petal.length') #橫軸名稱
    ax2.set_ylabel('petal.width') #縱軸名稱  
    ax2.legend()  #顯示圖例
    st.pyplot(fig2)

    