# -*- coding: utf-8 -*-
"""Rekomendasi Film Indonesia dengan Model Content Based Filtering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j3Mf1JhwKSlrRJyKHPsR0xiAlFcEStXi

# **Mengimpor Library yang Dibutuhkan**
Kode ini menyediakan pustaka yang umum digunakan untuk analisis data, visualisasi, dan pemrosesan teks dalam machine learning.
1. Pandas: Digunakan untuk manipulasi data berbentuk tabel (DataFrame), seperti pengolahan data, pembersihan data, dan analisis statistik.
2. Matplotlib.pyplot: Digunakan untuk membuat plot dan visualisasi data dalam bentuk grafik (seperti grafik batang, histogram, dll.).
3. Seaborn: Merupakan pustaka visualisasi berbasis Matplotlib yang menyediakan tampilan grafik yang lebih menarik dan mudah dipahami, terutama untuk analisis statistik.
4. TfidfVectorizer: Digunakan untuk mengonversi teks menjadi representasi numerik (vektor), berdasarkan frekuensi kata dan pentingnya kata dalam konteks seluruh kumpulan dokumen (melalui metode TF-IDF).
5. Cosine_similarity: menghitung kemiripan sudut antara vektor-vektor TF-IDF dari setiap dokumen dalam matriks. Nilai similarity berada dalam rentang 0 hingga 1, di mana 1 menunjukkan dokumen yang identik dan 0 menunjukkan dokumen yang sangat berbeda.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""# **Mengimpor Dataset**
Kode ini merupakan proses mengimpor dataset yang dibutuhkan dalam proyek ini. Sumber dataset yang digunakan pada proyek ini dari github "M. Irvan Dimetrio" (Tautan: https://github.com/IrvanDimetrio/IMDb-Movies-Analysis-in-Indonesia/blob/main/Data/Raw/imdb%20indonesia%20star.xlsx). File yang diimpor berbentuk excel, sehingga harus memanfaatkan fungsi dari library Pandas read_excel.
"""

df = pd.read_excel('imdb_indonesia_star.xlsx')
df

"""# **Tahap Data Understanding**
df.info() adalah metode yang digunakan untuk menampilkan informasi ringkas tentang sebuah DataFrame (df) di Pandas.
Dengan teknik ini akan menghasilkan beberapa hasil sebagai berikut ini.
- Jumlah baris (entries) dan kolom.
- Nama kolom dan tipe data setiap kolom.
- Jumlah nilai non-null untuk setiap kolom (untuk memeriksa adanya data yang hilang).
- Penggunaan memori untuk DataFrame.

Informasi di atas sangat bermanfaat untuk proses pengolahan data berikutnya.

"""

df.info()

"""df.describe() adalah fungsi yang digunakan untuk menghasilkan ringkasan statistik deskriptif dari DataFrame df. Fungsi ini memberikan informasi seperti:

- Count: Jumlah nilai non-null di setiap kolom.
- Mean: Rata-rata nilai numerik di setiap kolom.
- Std: Standar deviasi untuk mengukur sebaran nilai.
- Min: Nilai terkecil di setiap kolom.
- 25%, 50%, 75%: Kuartil pertama, median (kuartil kedua), dan kuartil ketiga.
- Max: Nilai terbesar di setiap kolom.

Fungsi ini memberikan gambaran umum distribusi data numerik dalam dataset pada kolom-kolom numerik saja.
"""

df.describe()

"""Kode ini untuk mendapatkan ringkasan statistik yang relevan pada kolom-kolom non-numerik, seperti:

- Count: Jumlah nilai non-null dalam kolom.
- Unique: Jumlah nilai unik dalam kolom.
- Top: Nilai yang paling sering muncul (frekuensi tertinggi).
- Freq: Frekuensi kemunculan nilai yang paling sering (nilai "Top").
"""

df.describe(include=['object'])

"""Kode ini menghitung dan menampilkan jumlah nilai yang hilang di setiap kolom dari DataFrame.
1. df.isnull(): Fungsi ini mengembalikan DataFrame baru yang berisi nilai boolean (True atau False) untuk setiap elemen dalam DataFrame df. Nilai True menunjukkan bahwa elemen tersebut adalah missing (NaN atau None), sementara False menunjukkan elemen tersebut memiliki nilai yang valid.

2. sum(): Fungsi ini digunakan untuk menjumlahkan nilai True dalam setiap kolom. Karena True dianggap sebagai 1 dan False sebagai 0, maka sum() menghitung jumlah nilai yang hilang (missing) di setiap kolom.

3. missing_values_count: Variabel ini menyimpan hasil perhitungan jumlah missing values per kolom dalam DataFrame df. Kemudian menampilkannya dalam bentuk tabel yang mudah dibaca.
"""

missing_values_count = df.isnull().sum()
missing_values_count

"""Kode ini digunakan untuk mencari dan menampilkan baris-baris yang duplikat dalam DataFrame df.

- df.duplicated(keep=False): Mengidentifikasi baris yang memiliki nilai duplikat di seluruh kolom, dengan keep=False menandakan semua duplikat dihitung.
- duplicate_rows = df[df.duplicated(keep=False)]: Menyaring baris-baris duplikat dan menyimpannya dalam variabel duplicate_rows.
- num_duplicate_rows = len(duplicate_rows): Menghitung jumlah baris yang berisi duplikat.
- print(f"Jumlah baris..."): Menampilkan jumlah baris yang duplikat.
- print("\nKolom yang..."): Menampilkan baris-baris yang duplikat dalam DataFrame.
"""

# Mencari nilai duplikat berdasarkan kolom
duplicate_rows = df[df.duplicated(keep=False)]

# Menghitung baris yang duplikat lalu menampilkan jumlahnya
num_duplicate_rows = len(duplicate_rows)

print(f"Jumlah baris yang berisi nilai duplikat ada sebanyak: {num_duplicate_rows}")

# Menampilkan seluruh baris dataset yang berisi nilai duplikat
print("\nKolom yang duplikat dan duplikasinya:")
duplicate_rows

"""Kode ini digunakan untuk mencari data yang memiliki judul film yang muncul dengan frekuensi lebih dari sekali dalam kolom 'Title'. Variabel `title_to_search` diisi dengan judul film yang dimaksudkan, dan kemudian `df[df['Title'] == title_to_search]` digunakan untuk memfilter baris-baris yang memiliki nilai yang sama pada kolom 'Title'. Hasilnya, variabel `filtered_df` akan berisi DataFrame yang hanya mencakup data dengan judul tersebut. Ini berguna untuk menganalisis atau mengeksplorasi karakteristik data berdasarkan film tertentu yang jumlah kemunculannya lebih dari sekali. Sehingga, dapat diolah sedemikian rupa."""

# Mengetahui karakteristik dari data dengan judul film yang sama
title_to_search = "Pulang"
filtered_df = df[df['Title'] == title_to_search]
filtered_df

"""Kode ini digunakan untuk membuat visualisasi frekuensi terhadap kolom non-numerik (kolom bertipe 'object') dalam DataFrame sebelum dilakukan tahap pra-pemrosesan data.

- Looping kolom: Kode ini melakukan iterasi untuk setiap kolom di DataFrame dan memeriksa apakah kolom tersebut bertipe 'object' (biasanya untuk data kategorikal).
- Menghitung frekuensi: Untuk kolom bertipe 'object', value_counts().nlargest(15) menghitung frekuensi kemunculan nilai dan memilih 15 nilai teratas.
- Membuat visualisasi: Menggunakan sns.barplot, kode ini menggambar grafik batang frekuensi nilai-nilai teratas, dengan rotasi label pada sumbu x sebesar 90 derajat.
- Menampilkan grafik: Setiap grafik diberi judul, label sumbu x dan y, dan kemudian ditampilkan menggunakan plt.show().
"""

# Membuat visualisasi frekuensi terhadap data-data non-numerik sebelum dilakukan pra-pemrosesan data
for col in df.columns:
  if df[col].dtype == 'object':
    top_15 = df[col].value_counts().nlargest(15)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_15.index, y=top_15.values)
    plt.xticks(rotation=90)
    plt.title(f'Top 15 Frequencies for {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

"""# **Tahap Pra-Pemrosesan Data**
Kode ini digunakan untuk menghapus baris-baris yang duplikat dalam DataFrame. Fungsi ini akan memeriksa setiap baris, dan jika ada baris yang identik dengan baris lainnya, hanya satu yang akan dipertahankan. Secara default, fungsi ini menghapus baris duplikat berdasarkan seluruh kolom. Hasilnya, DataFrame yang baru akan berisi hanya baris-baris unik, tanpa duplikat.
"""

# Menghapus kolom yang berisi nilai duplikat dengan baris lainnya
df = df.drop_duplicates()

"""Kode ini bertujuan untuk mengubah tipe data pada kolom "Runtime (Minutes)" menjadi float64. Pertama-tama dihilangkan terlebih dahulu kata "min" yang merupakan kependekan dari kata "minutes" supaya menjadi data numerik. Kemudian tipe datanya yang semula berupa objek diubah menjadi bertipe data float64."""

# Menghapus kata "min" dalam kolom "Runtime (Minutes)" lalu mengubahnya menjadi bertipe data float64 dan menampilkan dataframe tersebut.
df['Runtime (Minutes)'] = df['Runtime (Minutes)'].astype(str).str.replace('min', '')
df['Runtime (Minutes)'] = df['Runtime (Minutes)'].astype('float64')
df

"""Kode di atas digunakan untuk mengisi baris-baris yang memiliki nilai yang kosong.

1. **Mengisi baris yang kosong pada kolom 'Runtime (Minutes)' dengan nilai rata-rata.**
Kode ini mengonversi kolom 'Runtime (Minutes)' menjadi tipe data float dan menghitung rata-rata dari nilai-nilai yang ada. Rata-rata ini digunakan untuk mengisi nilai yang kosong (NaN) di kolom tersebut. Hal ini membantu menghindari kehilangan data dan menjaga keutuhan informasi pada kolom. Setelah menghitung rata-rata, baris yang memiliki nilai kosong pada kolom 'Runtime (Minutes)' akan diisi dengan nilai rata-rata tersebut. Fungsi fillna(mean_runtime) digunakan untuk menggantikan nilai kosong dengan rata-rata yang sudah dihitung. Dengan ini, data menjadi lebih lengkap dan konsisten.

2. **Mengisi NaN di kolom 'Rating' dengan modus.**
Modus (nilai yang paling sering muncul) pada kolom 'Rating' dihitung menggunakan mode(). Jika ada lebih dari satu modus, yang pertama dipilih untuk mengisi nilai yang kosong. Penggunaan modus sangat berguna untuk data kategori seperti rating yang biasanya memiliki nilai terbanyak.

3. **Mengisi NaN di kolom 'Votes' dengan modus lalu diubah menjadi bertipe data int64.**
Sama seperti kolom 'Rating', kolom 'Votes' juga diisi dengan modusnya untuk menggantikan nilai kosong. Setelah seluruhnya terisi lalu mengubah tipe data pada kolom ini menjadi bertipe data int64.

4. **Menampilkan informasi tentang DataFrame.** Ini memberikan gambaran umum tentang status data setelah pengisian nilai kosong.
"""

# Mengisi baris kosong pada kolom 'Runtime (Minutes)' dengan rata-rata
mean_runtime = df['Runtime (Minutes)'].astype(float).mean()
df['Runtime (Minutes)'] = df['Runtime (Minutes)'].fillna(mean_runtime)

# Mengisi baris kosong pada kolom 'Rating' dengan modus
rating_mode = df['Rating'].mode()[0]  # Get the first mode if multiple exist
df['Rating'] = df['Rating'].fillna(rating_mode)

# Mengisi baris kosong pada kolom 'Votes' dengan modus lalu mengubahnya menjadi bertipe data int64
votes_mode = df['Votes'].mode()[0]  # Get the first mode if multiple exist
df['Votes'] = df['Votes'].fillna(votes_mode)
df['Votes'] = df['Votes'].str.replace(',', '').astype('int64')

# Menampilkan informasi penting setiap kolom
df.info()

"""Kode ini digunakan untuk mengelompokkan data film berdasarkan judulnya dan kemudian mengolahnya dengan kriteria tertentu untuk memilih nilai yang representatif. Pertama, data dikelompokkan berdasarkan kolom 'Title' menggunakan groupby('Title'), yang menghasilkan grup-grup film dengan judul yang sama. Selanjutnya, fungsi aggregate_data digunakan untuk mengolah setiap grup film, dengan memilih nilai tertentu seperti tahun rilis (mengambil tahun tertinggi), kategori rating (mengambil modus), genre (menggabungkan dan memilih modus), runtime, rating, jumlah suara (votes), serta aktor dan sutradara (menggunakan modus atau memilih nilai pertama jika modus tidak ada). Setelah itu, grouped.apply(aggregate_data) diterapkan untuk setiap grup, menghasilkan DataFrame yang telah diolah sesuai dengan kriteria yang ditentukan. Hasil akhirnya disimpan dalam aggregated_df, dan reset_index() digunakan untuk mengatur ulang indeks agar data lebih mudah dibaca."""

# Mengelompokkan judul film yang frekuensi kemunculannya lebih dari sekali
grouped = df.groupby('Title')

# Kriteria tertentu yang digunakan untuk memilih atribut pada film yang memiliki jumlah kemunculan lebih dari sekali.
def aggregate_data(group):
    year = group['Year'].max()
    rated = group['Rated'].mode()[0]
    genres = ', '.join(group['Genre'].dropna().astype(str))
    genre = pd.Series(genres.split(', ')).mode()[0].strip()
    runtime = group['Runtime (Minutes)'].max()
    rating = group['Rating'].max()
    votes = group['Votes'].max()
    director = group['Director'].mode()[0] if len(group['Director'].mode()) > 0 else group['Director'].iloc[0] if len(group['Director']) > 0 else float('nan')
    star1 = group['Star 1'].mode()[0] if len(group['Star 1'].mode()) > 0 else group['Star 1'].iloc[0] if len(group['Star 1']) > 0 else float('nan')
    star2 = group['Star 2'].mode()[0] if len(group['Star 2'].mode()) > 0 else group['Star 2'].iloc[0] if len(group['Star 2']) > 0 else float('nan')
    star3 = group['Star 3'].mode()[0] if len(group['Star 3'].mode()) > 0 else group['Star 3'].iloc[0] if len(group['Star 3']) > 0 else float('nan')
    star4 = group['Star 4'].mode()[0] if len(group['Star 4'].mode()) > 0 else group['Star 4'].iloc[0] if len(group['Star 4']) > 0 else float('nan')

    return pd.Series({
        'Year': year,
        'Rated': rated,
        'Genre': genre,
        'Runtime (Minutes)': runtime,
        'Rating': rating,
        'Votes': votes,
        'Director': director,
        'Star 1': star1,
        'Star 2': star2,
        'Star 3': star3,
        'Star 4': star4,
    })

# Menyimpan hasil lalu menampilkannya
aggregated_df = grouped.apply(aggregate_data).reset_index()
aggregated_df

"""Kode ini digunakan untuk menghapus kolom 'Star 3' dan 'Star 4' dari DataFrame aggregated_df menggunakan drop(['Star 3', 'Star 4'], axis=1), yang menghapus kolom berdasarkan nama kolom. Setelah itu, dropna() digunakan untuk menghapus baris-baris yang memiliki nilai kosong (NaN) di seluruh kolom. Akhirnya, df.info() dipanggil untuk menampilkan informasi mengenai struktur DataFrame yang telah dibersihkan, termasuk jumlah baris dan kolom yang tersisa setelah penghapusan kolom dan baris dengan nilai kosong."""

# Menghapus kolom 'Star 3' and 'Star 4' dan baris yang memiliki nilai kosong
df = aggregated_df.drop(['Star 3', 'Star 4'], axis=1)
df = df.dropna()
df.info()

"""# **Tahap Visualisasi Data**
Kode ini digunakan untuk membuat visualisasi frekuensi terhadap kolom non-numerik (kolom bertipe 'object') dalam DataFrame setelah dilakukan tahap pra-pemrosesan data.

- Looping kolom: Kode ini melakukan iterasi untuk setiap kolom di DataFrame dan memeriksa apakah kolom tersebut bertipe 'object' (biasanya untuk data kategorikal).
- Menghitung frekuensi: Untuk kolom bertipe 'object', value_counts().nlargest(15) menghitung frekuensi kemunculan nilai dan memilih 15 nilai teratas.
- Membuat visualisasi: Menggunakan sns.barplot, kode ini menggambar grafik batang frekuensi nilai-nilai teratas, dengan rotasi label pada sumbu x sebesar 90 derajat.
- Menampilkan grafik: Setiap grafik diberi judul, label sumbu x dan y, dan kemudian ditampilkan menggunakan plt.show().
"""

# Membuat visualisasi frekuensi terhadap data-data non-numerik setelah tahap pra-pemrosesan data
for col in df.columns:
  if df[col].dtype == 'object':
    top_15 = df[col].value_counts().nlargest(15)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_15.index, y=top_15.values)
    plt.xticks(rotation=90)
    plt.title(f'Top 15 Frequencies for {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

"""# **Pembuatan Model Content Based Filtering**

Kode ini digunakan untuk menerapkan teknik TF-IDF (Term Frequency-Inverse Document Frequency) untuk mengubah teks menjadi representasi numerik yang dapat digunakan dalam analisis data.

- Inisialisasi TfidfVectorizer: TfidfVectorizer() digunakan untuk mengubah teks menjadi vektor fitur berdasarkan frekuensi kata dan relevansinya dalam dokumen.
- Mempersiapkan data untuk TF-IDF: Kolom-kolom yang relevan seperti 'Year', 'Rated', 'Genre', dll. dipilih dan digabungkan menjadi satu kolom teks yang disebut 'combined_text'. Semua nilai diubah menjadi tipe data string dan digabungkan menggunakan spasi.
- Menghitung IDF: Fungsi fit() pada tf menghitung nilai IDF (Inverse Document Frequency) berdasarkan kolom 'combined_text'.
- Mendapatkan nama fitur: get_feature_names_out() digunakan untuk mendapatkan nama fitur yang mewakili kata-kata atau istilah yang ada dalam model TF-IDF, yang diurutkan berdasarkan indeks integer.
"""

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Memilih kolom kombinasi untuk TF-IDF lalu mengubahnya menjadi tipe data string dan mengumpulkan dalam satu kolom
columns_for_tfidf = ['Year', 'Rated', 'Genre', 'Rating', 'Runtime (Minutes)', 'Rating', 'Votes', 'Director', 'Star 1', 'Star 2']
df_tfidf = df[columns_for_tfidf]
df_tfidf = df_tfidf.astype(str)
df_tfidf['combined_text'] = df_tfidf.apply(' '.join, axis=1)

# Melakukan perhitungan idf pada data
tf.fit(df_tfidf['combined_text'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

"""Kode ini digunakan untuk mengubah data teks menjadi representasi matriks menggunakan teknik TF-IDF.

- Fit dan transformasi: tf.fit_transform(df_tfidf['combined_text']) menghitung nilai TF-IDF untuk setiap kata dalam kolom 'combined_text' dan mengubahnya menjadi matriks numerik (TF-IDF matrix).
- Ukuran matriks: tfidf_matrix.shape digunakan untuk menampilkan ukuran matriks yang dihasilkan, yang menunjukkan jumlah baris (dokumen) dan kolom (fitur kata).
"""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(df_tfidf['combined_text'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""Kode ini digunakan untuk mengubah matriks sparse hasil dari TF-IDF menjadi matriks padat (dense matrix).

Fungsi todense() mengubah format matriks sparse (di mana banyak elemen bernilai nol) menjadi matriks penuh yang lebih mudah dibaca dan diproses, dengan semua nilai ditampilkan, termasuk nol. Hal ini memudahkan dalam visualisasi atau analisis data lebih lanjut, meskipun dapat mengonsumsi lebih banyak memori jika matriksnya besar.
"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""Kode ini digunakan untuk mengonversi matriks TF-IDF menjadi DataFrame dan menampilkan sampel data.

- Membuat DataFrame: pd.DataFrame(tfidf_matrix.todense(), columns=tf.get_feature_names_out(), index=df.Title) mengubah matriks TF-IDF menjadi DataFrame, dengan kolom-kolom yang mewakili kata-kata (fitur) dan indeks yang mewakili judul film dari kolom 'Title'.
- Sampling kolom dan baris: .sample(22, axis=1) memilih 22 kolom secara acak, sementara .sample(10, axis=0) memilih 10 baris secara acak dari DataFrame yang dihasilkan. Ini digunakan untuk melihat subset data yang lebih kecil dari matriks TF-IDF.
"""

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=df.Title
).sample(22, axis=1).sample(10, axis=0)

"""Kode ini digunakan untuk menghitung cosine similarity antara setiap pasangan dokumen dalam matriks TF-IDF.

- Cosine similarity: cosine_similarity(tfidf_matrix) menghitung kemiripan sudut antara vektor-vektor TF-IDF dari setiap dokumen dalam matriks. Nilai similarity berada dalam rentang 0 hingga 1, di mana 1 menunjukkan dokumen yang identik dan 0 menunjukkan dokumen yang sangat berbeda.
- Matriks hasil: Hasilnya adalah matriks berbentuk persegi yang menunjukkan nilai cosine similarity antara setiap pasangan dokumen dalam dataset.
"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Kode ini digunakan untuk membuat DataFrame yang memvisualisasikan matriks cosine similarity antara film-film berdasarkan fitur TF-IDF.

- Membuat DataFrame: pd.DataFrame(cosine_sim, index=df['Title'], columns=df['Title']) mengonversi matriks cosine similarity menjadi DataFrame, dengan baris dan kolom berupa judul film dari kolom 'Title', sehingga setiap sel menunjukkan tingkat kemiripan antara dua film.
- Melihat ukuran: print('Shape:', cosine_sim_df.shape) menampilkan ukuran DataFrame untuk mengetahui jumlah baris dan kolom yang ada.
- Sampling matrix: cosine_sim_df.sample(10, axis=1).sample(10, axis=0) mengambil sampel acak 10 kolom dan 10 baris dari matriks untuk melihat sebagian kecil dari matriks similarity.
"""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa judul film
cosine_sim_df = pd.DataFrame(cosine_sim, index=df['Title'], columns=df['Title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap atribut
cosine_sim_df.sample(10, axis=1).sample(10, axis=0)

"""Fungsi film_recommendations ini digunakan untuk memberikan rekomendasi film berdasarkan cosine similarity terhadap sebuah film yang diberikan.

- Mendapatkan indeks similarity: Fungsi dimulai dengan mencari indeks film yang paling mirip dengan film yang dicari (dengan judul Title) dalam matriks similarity (similarity_data). argpartition digunakan untuk mengurutkan dan memilih k film teratas yang paling mirip.
- Mengambil film dengan similarity terbesar: Indeks yang dihasilkan digunakan untuk mengambil film yang memiliki nilai similarity terbesar dengan film yang dicari, dan nama film tersebut disimpan dalam variabel closest.
- Menyaring hasil: Film yang dicari (Title) dihapus dari daftar rekomendasi menggunakan drop, agar tidak muncul dalam daftar hasil rekomendasi.
- Mengembalikan rekomendasi: Fungsi kemudian menggabungkan data film terkait (dari items) dengan hasil closest, dan menampilkan k rekomendasi teratas dalam bentuk DataFrame.
"""

def film_recommendations(Title, similarity_data=cosine_sim_df, items=df[['Title', 'Year', 'Rated', 'Genre', 'Rating', 'Runtime (Minutes)', 'Rating', 'Votes', 'Director', 'Star 1', 'Star 2']], k=10):
  index = similarity_data.loc[:,Title].to_numpy().argpartition(
  range(-1, -k, -1))
  closest = similarity_data.columns[index[-1:-(k+2):-1]]
  closest = closest.drop(Title, errors='ignore')
  return pd.DataFrame(closest).merge(items).head(k)

"""# **Tahap Evaluasi Model**
Kode tersebut digunakan untuk memfilter baris dalam DataFrame df yang memiliki judul film yang dimaksud pada kolom 'Title'. Fungsi eq() memeriksa apakah nilai di kolom 'Title' sama dengan judul film yang dimaksud. Ini menghasilkan serangkaian nilai boolean (True atau False). Kemudian, filter ini diterapkan pada DataFrame, sehingga hanya baris dengan nilai True (yaitu yang memiliki judul film yang dimaksud) yang ditampilkan.
"""

df[df.Title.eq('Ziarah')]

"""Kode ini digunakan untuk mendapatkan rekomendasi film yang mirip dengan film yang dimaksud berdasarkan cosine similarity.
Fungsi film_recommendations akan mencari film dengan kemiripan tertinggi terhadap judul film yang dimaksud menggunakan matriks cosine similarity yang telah dihitung sebelumnya.Fungsi ini akan mengembalikan daftar k film yang paling mirip, lengkap dengan informasi terkait seperti tahun, rating, genre, dan lainnya.
"""

# Mendapatkan rekomendasi film yang mirip dengan film "ziarah"
film_recommendations('Ziarah')