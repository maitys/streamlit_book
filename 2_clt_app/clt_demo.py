import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating the Central Limit Theorem with Streamlit') 
st.subheader('An App by Siddharth') 
st.write(('This app simulates a thousand coin flips using the chance of heads input below,'  
          'and then samples with replacement from that population and plots the histogram of the' 
          ' means of the samples, in order to illustrate the Central Limit Theorem!')) 


perc_heads = st.number_input(label = "Chance of Coins Landing on Heads", min_value = 0.0, max_value = 1.0, value = 0.5)
binom_dist = np.random.binomial(n=1, p=perc_heads, size=1000)

graph_title = st.text_input(label = "Graph Title")
                            
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means, density=True, facecolor='indianred', alpha=0.75, bins=20, edgecolor='black', range=[0,1])
plt.title(graph_title)
st.pyplot(fig)

fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means, density=True, facecolor='forestgreen', alpha=0.75, bins=30, edgecolor='black', range=[0,1])
plt.title(graph_title)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2 = plt.hist(list_of_means, density=True, facecolor='royalblue', alpha=0.75, bins=50, edgecolor='black', range=[0,1])
plt.title(graph_title)
st.pyplot(fig2)

# Resume at location 623