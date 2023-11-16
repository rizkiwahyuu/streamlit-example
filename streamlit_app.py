# Import library yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Menentukan pertanyaan bisnis
# ...

# Data Wrangling
# ...

# EDA dan Visualisasi
# ...

# Pertanyaan 1: Perbandingan penumpang pada hari libur dan hari kerja
st.markdown("## Pertanyaan 1: Perbandingan Penumpang pada Hari Libur dan Hari Kerja")
st.write("Grafik perbandingan pola penyewaan sepeda antara hari kerja dan hari libur.")

# Menampilkan grafik menggunakan Streamlit
hour_data['day_type'] = 'Working Day'
hour_data.loc[hour_data['holiday'] == 1, 'day_type'] = 'Holiday'

hourly_average = hour_data.groupby(['day_type', 'hr'])['cnt'].mean().unstack()

# Streamlit plot
st.line_chart(hourly_average.T)

# Pertanyaan 2: Pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda
st.markdown("## Pertanyaan 2: Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
st.write("Grafik bar menunjukkan rata-rata jumlah peminjaman sepeda berdasarkan kondisi cuaca.")

# Group data berdasarkan kondisi cuaca
weather_conditions = hour_data.groupby('weathersit').agg({'cnt': 'mean'}).reset_index()

# Mapping kode cuaca ke deskripsi
weather_conditions['weathersit'] = weather_conditions['weathersit'].map({
    1: 'Clear, Few clouds',
    2: 'Mist, Cloudy',
    3: 'Light Snow, Light Rain',
    4: 'Heavy Rain, Thunderstorm, Mist'
})

# Sorting data berdasarkan rata-rata jumlah peminjaman sepeda
weather_conditions = weather_conditions.sort_values(by='cnt', ascending=False)

# Streamlit plot
st.bar_chart(weather_conditions.set_index('weathersit'))

# Menampilkan informasi umum dataset
st.markdown("## Informasi Umum Dataset (Harian)")
st.write(day_data.info())

# Menampilkan statistik deskriptif untuk kolom tertentu
st.markdown("## Statistik Deskriptif (Harian)")
st.write(day_data[['temp', 'hum', 'windspeed', 'cnt']].describe())

# Menampilkan histogram dan boxplot
st.markdown("## Histogram dan Boxplot (Harian)")
fig, axes = plt.subplots(2, 2, figsize=(12, 6))

# Histogram suhu
sns.histplot(day_data['temp'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribusi Suhu (Temperature)')

# Histogram kelembaban
sns.histplot(day_data['hum'], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Distribusi Kelembaban (Humidity)')

# Histogram kecepatan angin
sns.histplot(day_data['windspeed'], bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Distribusi Kecepatan Angin (Windspeed)')

# Boxplot jumlah penyewaan
sns.boxplot(x='cnt', data=day_data, ax=axes[1, 1])
axes[1, 1].set_title('Boxplot Jumlah Penyewaan (Count)')

fig.tight_layout()
st.pyplot(fig)

# Menampilkan informasi umum dataset per jam
st.markdown("## Informasi Umum Dataset (Per Jam)")
st.write(hour_data.info())

# Menampilkan statistik deskriptif per jam untuk kolom tertentu
st.markdown("## Statistik Deskriptif (Per Jam)")
st.write(hour_data[['temp', 'hum', 'windspeed', 'cnt']].describe())

# Menampilkan histogram dan boxplot per jam
st.markdown("## Histogram dan Boxplot (Per Jam)")
fig, axes = plt.subplots(2, 2, figsize=(12, 6))

# Histogram suhu
sns.histplot(hour_data['temp'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribusi Suhu (Temperature)')

# Histogram kelembaban
sns.histplot(hour_data['hum'], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Distribusi Kelembaban (Humidity)')

# Histogram kecepatan angin
sns.histplot(hour_data['windspeed'], bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Distribusi Kecepatan Angin (Windspeed)')

# Boxplot jumlah penyewaan
sns.boxplot(x='cnt', data=hour_data, ax=axes[1, 1])
axes[1, 1].set_title('Boxplot Jumlah Penyewaan (Count)')

fig.tight_layout()
st.pyplot(fig)
