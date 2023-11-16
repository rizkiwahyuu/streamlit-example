import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
hour_data = pd.read_csv('hour.csv')
day_data = pd.read_csv('day.csv')

# Drop duplicates and NaN values
day_data.drop_duplicates(subset=['dteday'], keep='first', inplace=True)
hour_data.dropna(inplace=True)
day_data.dropna(inplace=True)

# Sidebar
st.sidebar.title('Bike Sharing Data Analysis')

# Data Overview
st.header('Data Overview')
st.subheader('Hourly Data')
st.write(hour_data.head())
st.subheader('Daily Data')
st.write(day_data.head())

# Descriptive Statistics
st.header('Descriptive Statistics')
st.subheader('Daily Data')
st.write(day_data[['temp', 'hum', 'windspeed', 'cnt']].describe())
st.subheader('Hourly Data')
st.write(hour_data[['temp', 'hum', 'windspeed', 'cnt']].describe())

# Distribution Plots
st.header('Distribution Plots')
st.subheader('Daily Data')
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.histplot(day_data['temp'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Temperature Distribution')

sns.histplot(day_data['hum'], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Humidity Distribution')

sns.histplot(day_data['windspeed'], bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Windspeed Distribution')

sns.boxplot(x='cnt', data=day_data, ax=axes[1, 1])
axes[1, 1].set_title('Bike Rental Count Boxplot')

st.pyplot(fig)

# Line Plot
st.header('Hourly Bike Rental Patterns')
hour_data['day_type'] = 'Working Day'
hour_data.loc[hour_data['holiday'] == 1, 'day_type'] = 'Holiday'
hourly_average = hour_data.groupby(['day_type', 'hr'])['cnt'].mean().unstack()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=hourly_average.T, ax=ax)
ax.set_title('Comparison of Bike Rental Patterns between Working Days and Holidays')
ax.set_xlabel('Hour')
ax.set_ylabel('Average Bike Rental Count')
ax.legend(title='Day')

st.pyplot(fig)

# Weather Impact
st.header('Weather Impact on Bike Rentals')
weather_conditions = data.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()
weather_conditions['weathersit'] = weather_conditions['weathersit'].map({
    1: 'Clear, Few clouds',
    2: 'Mist, Cloudy',
    3: 'Light Snow, Light Rain',
    4: 'Heavy Rain, Thunderstorm, Mist'
})
weather_conditions = weather_conditions.sort_values(by='cnt', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_conditions, color='skyblue', ax=ax)
ax.set_xlabel('Weather Conditions')
ax.set_ylabel('Average Bike Rental Count')
ax.set_title('Impact of Weather Conditions on Bike Rentals')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

st.pyplot(fig)
