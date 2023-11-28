import streamlit as st
import pandas as pd
import requests
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from io import BytesIO

# Load the pre-trained k-Nearest Neighbors model
data = pd.read_csv('pyhton/data encodning.xlsx')
x = data[['Umur', 'Jenis Kelamin', 'Pendidikan']]
y = data['Pekerjaan']
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(x, y)

# Streamlit app
st.title('Prediksi Pekerjaan di Dusun Kerdon')
st.caption("Prediksi tersebut berdasarakan hasil sensus dan menggunakan Algoritma K-Nearest Neighbors (KNN) dengan N = 5 ")
st.caption("Dengan Tingkat Akurasi Sebesar 54%")
st.caption("[Link Perhitungan Akurasi](https://colab.research.google.com/drive/1PhvQCkMgGbFZ-baIBjChP3LyFUw1Kpkp?usp=sharing)")
st.empty()
# Pertanyaan Pertama
st.subheader("Masukan Umur")
umur_options = { "0-6" : 1, "7-18" : 2, "18-56": 3 ,">56":  4}
# User input for Umur using st.radio
umur = st.selectbox("Umur", (umur_options.keys()))

# Pertanyaan Kedua
st.subheader("Masukan Jenis Kelamin")
kelamin_options = {"Laki Laki": 1, "Perempuan": 2}
kelamin = st.selectbox("Jenis Kelamin", kelamin_options.keys())

# Pertanyaan Ketiga
st.subheader("Masukan Pendidikan Terakhir")
pendidikan_options = {"SD": 1, "SMP": 2, "SMA/K": 3, "Kuliah": 4}
pendidikan = st.selectbox("Pendidikan", pendidikan_options.keys())

# Map user input to numerical values
umur_value = umur_options[umur]
kelamin_value = kelamin_options[kelamin]
pendidikan_value = pendidikan_options[pendidikan]
# User input data
input_data = [[umur_value, kelamin_value, pendidikan_value]]

st.empty()
# Button to show the result on a new page
if st.button('Lihat Hasil Prediksi'):

  # New page for displaying result
  st.markdown('# Hasil Prediksi Pekerjaan')
  # Perform prediction
  prediction = knn_model.predict(input_data)
  st.write(f'Pekerjaan yang diprediksi: {prediction[0]}')


  # Mapping between job names and image URLs
  job_images = {
      'Petani': 'https://img.freepik.com/free-vector/organic-farming-concept-with-man-using-digger_23-2148439678.jpg?w=740&t=st=1701164502~exp=1701165102~hmac=406ab1501c6478a1f94d7fe9aa7fd885b31355d280d978a480bfb69f3731370d',
      'Wirausaha': 'https://img.freepik.com/free-vector/salesman-composition-with-flat-design_23-2147872974.jpg?w=740&t=st=1701164461~exp=1701165061~hmac=f275da8df38b95605e28cd862ae9d7cf16b31457059ff0d1bf7cb0d97aea6348',
      'Lain-Lain': 'https://img.freepik.com/free-vector/collection-big-set-isolated-various-occupations-profession-people-wearing-professional-uniform-flat-illustration_1150-37448.jpg?w=740&t=st=1701164386~exp=1701164986~hmac=abb25c2c2831dcaf8ae200d672dd913eff83ee8ec66d522b883f639db7eb8a3a',
      'PNS': 'https://img.freepik.com/free-vector/illustration-character-civil-servants-indonesia-wearing-work-uniforms_10045-683.jpg?w=740&t=st=1701164268~exp=1701164868~hmac=0bd07b0206bfe9afce1d91bfd94730a3e63773803be16fdd2182e3e1e6c9cca5',
      'Buruh': 'https://img.freepik.com/free-vector/construction-worker-uniform_1308-99642.jpg?size=626&ext=jpg&ga=GA1.1.1095556142.1701164245&semt=ais',
  }
  # Display image based on the predicted job
  if prediction[0] in job_images:
      image_url = job_images[prediction[0]]
      image = Image.open(BytesIO(requests.get(image_url).content))
      st.image(image)
  else:
      st.warning(f'Tidak ada gambar yang tersedia untuk pekerjaan: {prediction[0]}')


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
