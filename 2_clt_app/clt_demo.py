import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

binom_dist = np.random.binomial(n=1, p=0.5, size=1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means, density=True, facecolor='indianred', alpha=0.75, bins=20, edgecolor='black')
st.pyplot(fig)

fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means, density=True, facecolor='forestgreen', alpha=0.75, bins=20, edgecolor='black')
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2 = plt.hist(list_of_means, density=True, facecolor='royalblue', alpha=0.75, bins=30, edgecolor='black')
st.pyplot(fig2)

# Resume location 530