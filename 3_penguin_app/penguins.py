import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Palmers's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!') 

# Selections
selected_species = st.selectbox(label = "What species would you like to visualize?", 
                                options = ["Adelie", "Gentoo", "Chinstrap"])
selected_x_var = st.selectbox(label = 'What do want the x variable to be?', 
                              options = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 
selected_y_var = st.selectbox(label = 'What about the y?', 
                              options = ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']) 
# Import Data
penguins_df = pd.read_csv(r"3_penguin_app\penguins.csv")
penguins_df = penguins_df[penguins_df["species"] == selected_species]

fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var], y = penguins_df[selected_y_var], color='indianred', edgecolor="black")
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of {}".format(selected_species))
plt.grid(linestyle="dashed")
st.pyplot(fig)

# Resume at 752

