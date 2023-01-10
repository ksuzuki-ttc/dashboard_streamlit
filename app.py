import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

'''
### 正規分布

母数（パラメータ）を変化させたときのグラフの変化の確認
'''

## 期待値と分散を指定
mu = st.sidebar.slider('期待値', min_value=-5.0, max_value=5.0, step=0.01)
sigma = st.sidebar.slider('分散', min_value=0, max_value=20, step=1)

## 標準正規分布の描画
x_1 = np.linspace(-10, 10, 100)
z = stats.norm.pdf(x_1, mu, sigma)
fig_norm, ax1 = plt.subplots()
ax1.plot(x_1, z, label='std_norm')
ax1.legend()
st.pyplot(fig_norm)

'''
### ポアソン分布

母数（パラメータ）を変化させたときのグラフの変化の確認
'''

## 期待値と分散を指定
lam = st.sidebar.slider('期待値', min_value=0, max_value=30, step=1)

## ポアソン分布の描画
x_2 = np.linspace(0, 30, 31)
r = stats.poisson.pmf(x_2, lam)
fig_pois, ax2 = plt.subplots()
ax2.bar(x_2, height=r, color='#00A968', label='poisson')
ax2.legend()
st.pyplot(fig_pois)
