import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

hour_data = pd.read_csv('hour.csv')
day_data = pd.read_csv('day.csv')

print("Data Per Jam:")
print(hour_data.head())
print("Data Per Hari:")
print(day_data.head())
day_data.drop_duplicates(subset=['dteday'], keep='first', inplace=True)
hour_data.dropna(inplace=True)
day_data.dropna(inplace=True)


print("Informasi Umum Dataset (Harian):")
print(day_data.info())

print("\nStatistik Deskriptif:")
print(day_data[['temp', 'hum', 'windspeed', 'cnt']].describe())

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.histplot(day_data['temp'], bins=20, kde=True)
plt.title('Distribusi Suhu (Temperature)')

plt.subplot(2, 2, 2)
sns.histplot(day_data['hum'], bins=20, kde=True)
plt.title('Distribusi Kelembaban (Humidity)')

plt.subplot(2, 2, 3)
sns.histplot(day_data['windspeed'], bins=20, kde=True)
plt.title('Distribusi Kecepatan Angin (Windspeed)')

plt.subplot(2, 2, 4)
sns.boxplot(x='cnt', data=day_data)
plt.title('Boxplot Jumlah Penyewaan (Count)')

plt.tight_layout()
plt.show()

print("Informasi Umum Dataset:")
print(hour_data.info())

print("\nStatistik Deskriptif:")
print(hour_data[['temp', 'hum', 'windspeed', 'cnt']].describe())

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.histplot(hour_data['temp'], bins=20, kde=True)
plt.title('Distribusi Suhu (Temperature)')

plt.subplot(2, 2, 2)
sns.histplot(hour_data['hum'], bins=20, kde=True)
plt.title('Distribusi Kelembaban (Humidity)')

plt.subplot(2, 2, 3)
sns.histplot(hour_data['windspeed'], bins=20, kde=True)
plt.title('Distribusi Kecepatan Angin (Windspeed)')

plt.subplot(2, 2, 4)
sns.boxplot(x='cnt', data=hour_data)
plt.title('Boxplot Jumlah Penyewaan (Count)')

plt.tight_layout()
plt.show()

hour_data['day_type'] = 'Working Day'
hour_data.loc[hour_data['holiday'] == 1, 'day_type'] = 'Holiday'
hourly_average = hour_data.groupby(['day_type', 'hr'])['cnt'].mean().unstack()

plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_average.T)
plt.title('Perbandingan Pola Penyewaan Sepeda antara Hari Kerja dan Hari Libur')
plt.xlabel('Jam (Hour)')
plt.ylabel('Rata-rata Jumlah Penyewaan (Count)')
plt.legend(title='Hari')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hour.csv")
weather_conditions = data.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()
weather_conditions['weathersit'] = weather_conditions['weathersit'].map({
    1: 'Clear, Few clouds',
    2: 'Mist, Cloudy',
    3: 'Light Snow, Light Rain',
    4: 'Heavy Rain, Thunderstorm, Mist'
})
weather_conditions = weather_conditions.sort_values(by='cnt', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(weather_conditions['weathersit'], weather_conditions['cnt'], color='skyblue')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')
plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda')
plt.xticks(rotation=45, ha='right')  # Rotasi label agar lebih mudah dibaca
plt.tight_layout()
plt.show()
