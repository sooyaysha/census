import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title.sidebar('Census Data Visualization')
# Using the 'if' statement, display raw data on the click of the checkbox.
data = st.checkbox('Display Raw Data')
if data:
  st.write(census_data)
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
visualization_options = st.multiselect('Visualization Selector: ', ['Pie-Chart', 'Boxplot', 'Bar Chart'])

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
visualization_options = plot_list

# Display pie plot using matplotlib module and 'st.pyplot()'
if visualization_options = 'Pie-Chart':
  labels_income = census_df['income-group'].unique()
  data_income = census_df['income-group'].value_counts()
  plt.figure(figsize = (6,6), dpi = 96)
  ax = plt.pie(data_income, labels_income = labels)
  st.pyplot(ax)
  labels_gender = census_df['gender'].unique()
  data_gender = census_df['gender'].value_counts()
  plt.figure(figsize = (6,6), dpi = 96)
  ax1 = plt.pie(data_gender, labels_gender = labels)
  st.pyplot(ax1)

# Display box plot using matplotlib module and 'st.pyplot()'
if visualization_options = 'Boxplot':
  plt.figure(figsize = (12,5))
  ax = plt.boxplot(census_df['hours-per-week'])
  st.pyplot(ax)

# Display count plot using seaborn module and 'st.pyplot()' 
if visualization_options = 'Bar Chart':
  plt.figure(figsize= (12,5))
  ax = sns.countplot(x = 'workclass', data = census_df)
  st.pyplot(ax)