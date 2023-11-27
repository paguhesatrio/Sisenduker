import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from io import BytesIO
from PIL import Image

sns.set(style='dark')

all_df = pd.read_csv('pyhton/Semua Data.csv')

# =================== Header
st.header('Visualisasi Data Sensus Dusun Kerdon Feb 2023')
st.markdown("[Link Hasil Analisis Sensus Dusun Kerdon](https://colab.research.google.com/drive/16yIYD1ChjmQfnfoDDtWjpRfrwDZZMj91?usp=sharing)", unsafe_allow_html=True)
# =================== Header

#============================================================================================== Perbandingan Laki-laki dan Perempuan
def gender(df):
    laki = df['L'].sum()
    cewe = df['P'].sum()
    jumlahGender = laki + cewe
    return laki , cewe , jumlahGender

# Subheader
st.subheader("Perbandingan Laki-laki dan Perempuan")
col1, col2 , col3= st.columns(3)

with col1:
    laki_df, _, _ = gender(all_df)
    st.markdown(f"Jumlah Laki Laki : **{laki_df}**")

with col2:
     _, cewe_df, _ = gender(all_df)
     st.markdown(f"Jumlah Perempuan : **{cewe_df}**")

with col3:
   _, _, jumlahGender_df = gender(all_df)
   st.markdown(f"Jumlah Semua : **{jumlahGender_df}**")

labels = ['Laki-laki', 'Perempuan']
sizes = [laki_df, cewe_df]
colors = ['#D3D3D3', '#068DA9']

fig, ax = plt.subplots(figsize=(16, 8))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  

ax.set_title("Grafik Customer Setiap Sate", fontsize=15)
st.pyplot(fig)
#============================================================================================== Perbandingan Laki-laki dan Perempuan

#============================================================================================== Perbandingan umur
def umur(df):
    umur1 = df['0-6'].sum()
    umur2 = df['7 s/d 18'].sum()
    umur3 = df['18 s/d 56'].sum()
    umur4 = df['>56'].sum()
    return  umur1, umur2, umur3, umur4

# Subheader
st.subheader("Perbandingan Umur")
col1, col2 , col3, col4 = st.columns(4)

with col1:
    umur1, _, _, _ = umur(all_df)
    st.markdown(f"Umur 0-6 : **{umur1}**")

with col2:
    _, umur2, _, _ = umur(all_df)
    st.markdown(f"Umur 7 s/d 18 : **{umur2}**")

with col3:
    _,  _, umur3, _ = umur(all_df)
    st.markdown(f"Umur 18 s/d 56 : **{umur3}**")

with col4:
    _,  _, _,umur4 = umur(all_df)
    st.markdown(f"Umur >56 : **{umur4}**")

# Plot Bar
colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Buat DataFrame untuk plot
umur_df = pd.DataFrame({
    'Umur': ['0-6', '7 s/d 18', '18 s/d 56', '>56'],
    'Jumlah': [umur1, umur2, umur3, umur4],
})

# Urutkan DataFrame berdasarkan jumlah secara menurun
umur_df_sorted = umur_df.sort_values(by='Jumlah', ascending=False)

# Plot Bar
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='Umur', y='Jumlah', data=umur_df_sorted, palette=colors, ax=ax)
ax.set_title("Perbandingan Umur")
ax.set_xlabel("Rentang Umur")
ax.set_ylabel("Jumlah")
st.pyplot(fig)
#============================================================================================== Perbandingan umur

#============================================================================================== Perbandingan pendidikan
def pendidikan(df):
    sd = df['Sd'].sum()
    smp = df['SMP'].sum()
    sma = df['SMA/K'].sum()
    kuliah = df['Kuliah'].sum()
    return  sd, smp, sma, kuliah

# Subheader
st.subheader("Perbandingan pendidikan")
col1, col2 , col3, col4 = st.columns(4)

with col1:
    sd, _, _, _ = pendidikan(all_df)
    st.markdown(f"pendidikan SD: **{sd}**")

with col2:
    _, smp, _, _ = pendidikan(all_df)
    st.markdown(f"pendidikan SMP : **{smp}**")

with col3:
    _,  _, sma, _ = pendidikan(all_df)
    st.markdown(f"pendidikan SMA : **{sma}**")

with col4:
    _,  _, _,kuliah = pendidikan(all_df)
    st.markdown(f"pendidikan Kuliah : **{kuliah}**")

# Plot Bar
colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Buat DataFrame untuk plot
umur_df = pd.DataFrame({
    'Umur': ['Sd', 'SMP', 'SMA/K', 'Kuliah'],
    'Jumlah': [sd, smp, sma, kuliah],
})

# Urutkan DataFrame berdasarkan jumlah secara menurun
umur_df_sorted = umur_df.sort_values(by='Jumlah', ascending=False)

# Plot Bar
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='Umur', y='Jumlah', data=umur_df_sorted, palette=colors, ax=ax)
ax.set_title("Perbandingan pendidikan")
ax.set_xlabel("Rentang Pendidikan")
ax.set_ylabel("Jumlah")
st.pyplot(fig)
#============================================================================================== Perbandingan pendidikan


#============================================================================================== Perbandingan pekerjaan
def pekerjaan(df):
    sd = df['PNS'].sum()
    smp = df['Petani'].sum()
    sma = df['Buruh'].sum()
    kuliah = df['Wirausaha'].sum()
    lain = df['Lain-lain'].sum()
    return  sd, smp, sma, kuliah, lain

# Subheader
st.subheader("Perbandingan pekerjaan")
col1, col2 , col3, col4, col5 = st.columns(5)

with col1:
    sd, _, _, _ ,_ = pekerjaan(all_df)
    st.markdown(f"pekerjaan PNS: **{sd}**")

with col2:
    _, smp, _, _ ,_  = pekerjaan(all_df)
    st.markdown(f"pekerjaan Petani : **{smp}**")

with col3:
    _,  _, sma, _ ,_ = pekerjaan(all_df)
    st.markdown(f"pekerjaan Buruh : **{sma}**")

with col4:
    _,  _, _,kuliah,_  = pekerjaan(all_df)
    st.markdown(f"pekerjaan Wirausaha : **{kuliah}**")


with col5:
    _,  _, _,_, lain = pekerjaan(all_df)
    st.markdown(f"pekerjaan Lain Lain : **{lain}**")

# Plot Bar
colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Buat DataFrame untuk plot
umur_df = pd.DataFrame({
    'Umur': ['PNS', 'Petani', 'Buruh', 'Wirausaha', 'Lain-lain'],
    'Jumlah': [sd, smp, sma, kuliah, lain],
})

# Urutkan DataFrame berdasarkan jumlah secara menurun
umur_df_sorted = umur_df.sort_values(by='Jumlah', ascending=False)

# Plot Bar
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='Umur', y='Jumlah', data=umur_df_sorted, palette=colors, ax=ax)
ax.set_title("Perbandingan Pekerjaan")
ax.set_xlabel("Rentang Pekerjaan")
ax.set_ylabel("Jumlah")
st.pyplot(fig)
#============================================================================================== Perbandingan pendidikan


# Load your data
new_df = pd.read_csv('pyhton/data Baru.csv')

#============================================================================================== Perbandingan pendidikan dan pekerjaan   
st.subheader("Perbandingan antara Pekerjaan dan Pendidikan")

def bayarSt(df):
    bayarSt = df.groupby(["Pendidikan", "Pekerjaan"]) ["Pekerjaan"].size().reset_index(name='Jumlah')
    return bayarSt

# Mendapatkan data pembayaran per pendidikan dan pekerjaan
bayarSt_df = bayarSt(new_df)

# Sorting berdasarkan jumlah pembayaran terbanyak
bayarSt_df = bayarSt_df.sort_values(by='Jumlah', ascending=False)

# Membuat plot dengan Seaborn
plt.figure(figsize=(16, 8))
sns.barplot(x='Pekerjaan', y='Jumlah', hue='Pendidikan', data=bayarSt_df)

plt.title("Grafik Perbandingan antara Pendidikan dan Pekerjaan", fontsize=15)
plt.ylabel("Jumlah")
plt.xlabel("Pekerjaan")
plt.xticks(fontsize=10)
plt.legend(title="Pendidikan")
plt.yticks(fontsize=10)

# Menampilkan plot di Streamlit
st.pyplot(plt)
#============================================================================================== Perbandingan pendidikan dan pekerjaan   

#============================================================================================== Perbandingan Umur dan pekerjaan
st.subheader("Perbandingan antara Pekerjaan dan Umur")

def bayarSt(df):
    bayarSt = df.groupby(["Umur", "Pekerjaan"]) ["Pekerjaan"].size().reset_index(name='Jumlah')
    return bayarSt

# Mendapatkan data pembayaran per Umur dan pekerjaan
bayarSt_df = bayarSt(new_df)

# Sorting berdasarkan jumlah pembayaran terbanyak
bayarSt_df = bayarSt_df.sort_values(by='Jumlah', ascending=False)

# Membuat plot dengan Seaborn
plt.figure(figsize=(16, 8))
sns.barplot(x='Pekerjaan', y='Jumlah', hue='Umur', data=bayarSt_df)

plt.title("Grafik Perbandingan antara Umur dan Pekerjaan", fontsize=15)
plt.ylabel("Jumlah")
plt.xlabel("Pekerjaan")
plt.xticks(fontsize=10)
plt.legend(title="Umur")
plt.yticks(fontsize=10)

# Menampilkan plot di Streamlit
st.pyplot(plt)
#============================================================================================== Perbandingan Umur dan pekerjaan


with st.sidebar:
    # Menambahkan logo perusahaan
    from PIL import Image
    image = Image.open('img/logo.png')
    st.image(image)
    st.markdown("[Home](https://sisenduker.000webhostapp.com/)", unsafe_allow_html=True)
    st.markdown("[Lihat Sensus](https://sisenduker.000webhostapp.com/semua.html)", unsafe_allow_html=True)
    st.markdown("[Analisis](https://sisenduker.streamlit.app/)", unsafe_allow_html=True)
    st.markdown("[Prediksi]( )", unsafe_allow_html=True)
    st.markdown("[Galeri](https://sisenduker.000webhostapp.com/galeri.html)", unsafe_allow_html=True)
    st.markdown("[Tentang Kami](https://sisenduker.000webhostapp.com/service.html)", unsafe_allow_html=True)
    st.write('Copyright (C) © 2023 by Paguh')


