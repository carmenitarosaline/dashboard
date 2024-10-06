import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://media.licdn.com/dms/image/v2/D5603AQGCgwGV3HObkg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1706328507364?e=1733356800&v=beta&t=LftcEbpSvRPbZQuvkbGzHVCCxc-1kdVxp5BZHiC3WSg")
    st.write(
    """
    # Carmenita Lamba
    Bangkit Student ID	  :  	M309B4KX2298
    """
)
# header
st.header('Welcome To')

# Load the dataset
data = pd.read_csv('all_data.csv')

# Title of the dashboard
st.title('Bike Sharing Analysis Dashboard')

# Bar chart for weather conditions and bike usage
st.header('Pengaruh Kondisi Cuaca terhadap Jumlah Pengguna Sepeda')


# Load dataset
data = pd.read_csv('all_data.csv')

# Pastikan dataset memiliki kolom 'dteday' yang berisi tanggal
if 'dteday' in data.columns:
    # Konversi kolom 'dteday' ke tipe datetime
    data['dteday'] = pd.to_datetime(data['dteday'])
    
    # Filter berdasarkan rentang tanggal yang dipilih oleh pengguna
    st.sidebar.header('Filter Data')
    start_date = st.sidebar.date_input("Start date", data['dteday'].min())
    end_date = st.sidebar.date_input("End date", data['dteday'].max())
    
    if start_date > end_date:
        st.sidebar.error("Tanggal mulai tidak boleh lebih besar dari tanggal akhir.")
    else:
        # Filter data sesuai rentang tanggal
        filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

# Pastikan kolom yang digunakan ada dan sesuai
if 'weathersit' in data.columns and 'cnt' in data.columns:
    # Group data by 'weathersit' dan hitung rata-rata 'cnt'
    weather_grouped = data.groupby('weathersit')['cnt'].mean().reset_index()

    # Membuat mapping kondisi cuaca menjadi label kategorikal
    weather_labels = {
        1: 'Clear',
        2: 'Misty/Cloudy',
        3: 'Light Snow/Rain',
        4: 'Heavy Rain/Snow'
    }

    # Ganti angka dengan deskripsi kondisi cuaca
    weather_grouped['weathersit'] = weather_grouped['weathersit'].map(weather_labels)

    # Plot bar chart dengan label cuaca
    fig, ax = plt.subplots()
    ax.bar(weather_grouped['weathersit'], weather_grouped['cnt'], color='blue')
    ax.set_xlabel('Kondisi Cuaca (weathersit)')
    ax.set_ylabel('Rata-rata Pengguna Sepeda (cnt)')
    ax.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Total Pengguna Sepeda (cnt)')
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.error("Kolom 'weathersit' atau 'cnt' tidak ditemukan dalam dataset.")

# Pie chart for workday vs non-workday usage
st.header('Perbandingan Penggunaan Sepeda: Hari Kerja vs Non-Hari Kerja')

# Group data by workingday
workday_grouped = data.groupby('workingday')['cnt'].sum().reset_index()

# Plot pie chart
fig, ax = plt.subplots()
ax.pie(workday_grouped['cnt'], labels=['Non-Working Day', 'Working Day'], autopct='%1.1f%%', colors=['orange', 'lightblue'])
ax.set_title('Perbandingan Penggunaan Sepeda: Hari Kerja vs Non-Hari Kerja')
st.pyplot(fig)

st.caption('Copyright (c) Carmenita Lamba 2024')