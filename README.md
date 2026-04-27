# Proyek Analisis Data: Bike Sharing

Proyek ini bertujuan untuk menganalisis pola penggunaan layanan bike sharing berdasarkan faktor waktu, musim, dan kondisi cuaca. Analisis dilakukan menggunakan pendekatan *Exploratory Data Analysis (EDA)* dan divisualisasikan melalui dashboard interaktif menggunakan Streamlit.

Proyek ini dibuat sebagai bagian dari submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.

---

## Deskripsi Proyek

Dalam analisis ini, beberapa pertanyaan bisnis yang ingin dijawab adalah:

1. Berapa persentase perbedaan rata-rata penyewa sepeda pengguna *registered* pada jam sibuk (07:00–09:00 dan 17:00–19:00) dibandingkan jam kerja biasa pada hari kerja (Senin–Jumat) selama tahun 2012?

2. Seberapa besar persentase penurunan rata-rata total penyewa harian (*cnt*) saat kondisi cuaca berubah dari *Clear* menjadi *Light Snow* selama musim dingin (*winter*) pada tahun 2011–2012?

3. Berapa tingkat pertumbuhan pengguna *casual* di akhir pekan pada musim panas (*summer*) dibandingkan musim semi (*spring*) pada tahun 2012?

Melalui pertanyaan-pertanyaan tersebut, diharapkan dapat diperoleh insight mengenai perilaku pengguna sepeda, baik untuk kebutuhan commuting maupun rekreasi.

---

## Setup Environment

```bash
### Menggunakan Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

### Menggunakan Shell/Terminal
cd submission
python -m venv venv
venv\Scripts\activate   # untuk Windows
pip install -r requirements.txt

### Menjalankan Dashboard
cd dashboard
streamlit run dashboard.py
