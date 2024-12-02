# Laporan Proyek Machine Learning Sistem Rekomendasi Film - Suhardi

## Project Overview

Dalam era digital yang semakin maju, industri hiburan, khususnya film, telah mengalami transformasi besar. Platform streaming seperti Netflix, Disney+, dan layanan lokal lainnya telah menjadi salah satu pilihan utama bagi masyarakat untuk menikmati berbagai konten hiburan. Namun, dengan banyaknya pilihan film yang tersedia, pengguna sering kali kesulitan menemukan konten yang sesuai dengan selera mereka. Di sinilah sistem rekomendasi berperan penting. Sistem rekomendasi adalah salah satu alat yang dapat membantu mempersonalisasi pengalaman pengguna dengan memberikan saran konten berdasarkan preferensi individu.

Salah satu metode yang banyak digunakan dalam sistem rekomendasi adalah content-based filtering. Metode ini memanfaatkan atribut dari konten, seperti genre, tahun rilis, pemeran, durasi, dan beberapa hal lainnya untuk menyusun rekomendasi. Content-based filtering bekerja dengan cara membandingkan karakteristik film yang sudah disukai pengguna dengan film lainnya. Misalnya, jika seorang pengguna menyukai film bergenre horor dengan durasi singkat, sistem akan merekomendasikan film horor lainnya yang memiliki durasi serupa. Hal ini memberikan pengalaman yang lebih personal dan relevan bagi pengguna.

**Proyek ini penting untuk diselesaikan karena memiliki beberapa manfaat yang signifikan diantaranya adalah sebagai berikut ini.**

Pertama, sistem ini dapat meningkatkan personalisasi pengalaman pengguna. Pengguna tidak perlu lagi membuang waktu untuk mencari film yang sesuai dengan selera mereka. Sebaliknya, mereka akan disajikan dengan rekomendasi film yang kemungkinan besar akan mereka nikmati. Personalisasi semacam ini penting dalam membangun hubungan yang kuat antara platform dan pengguna, sehingga mendorong loyalitas pengguna.
Kedua, sistem rekomendasi ini dapat meningkatkan waktu tonton pengguna. Dengan menampilkan konten yang sesuai dengan preferensi mereka, pengguna cenderung menghabiskan lebih banyak waktu di platform. Ini tidak hanya meningkatkan kepuasan pengguna tetapi juga memberikan keuntungan bagi platform dalam bentuk peningkatan pendapatan, baik dari iklan maupun langganan. Semakin tinggi waktu tonton, semakin besar peluang bagi platform untuk mempertahankan dan memperluas basis penggunanya.
Ketiga, proyek ini memanfaatkan data metadata film secara optimal. Data seperti genre, tahun rilis, sutradara, pemeran, dan rating adalah sumber informasi yang sangat berharga. Dengan memanfaatkan data ini, sistem rekomendasi dapat menghasilkan wawasan yang berguna tidak hanya untuk pengguna, tetapi juga bagi produser dan pembuat konten. Mereka dapat memahami tren preferensi penonton dan menyesuaikan produksi mereka untuk memenuhi permintaan pasar.

proyek sistem rekomendasi berbasis content-based filtering memiliki nilai strategis yang besar. Dengan membantu pengguna menemukan film yang sesuai dengan preferensi mereka, sistem ini tidak hanya meningkatkan pengalaman pengguna, tetapi juga memberikan manfaat yang luas bagi industri hiburan secara keseluruhan. Oleh karena itu, penyelesaian proyek ini merupakan langkah penting untuk menghadirkan solusi inovatif yang relevan dengan kebutuhan masyarakat digital saat ini.

## Business Understanding

Beberapa permasalahan dalam memberikan rekomendasi untuk menonton suatu film akan diselesaikan dalam proyek ini. Berikut ini perincian permasalahan dan tujuannya.

### Problem Statements

**Permasalah pertama:**
Pengguna kesulitan menemukan film yang sesuai dengan preferensi mereka di tengah ribuan pilihan yang tersedia di platform streaming. Hal ini menyebabkan pengalaman menonton menjadi kurang efektif dan membosankan, yang dapat mengurangi waktu yang dihabiskan pengguna di platform.

**Permasalah kedua:**
Model yang memanfaatkan metadata film kurang optimal karena tingkat presisi model masih di bawah 75 persen. Sehingga akan banyak menghasilkan rekomendasi-rekomendasi yang tidak sesuai dengan preferensi pengguna. 

**Permasalah ketiga:**
Film-film lokal, terutama yang memiliki nilai seni tinggi tetapi kurang populer, sering kali kurang terekspos kepada pengguna. Ini berdampak pada rendahnya apresiasi dan dukungan terhadap karya lokal.


### Goals

Tujuan utama proyek ini untuk beberapa hal di bawah ini.

**1. Jawaban Pernyataan Masalah Pertama:** Membangun sistem rekomendasi berbasis content-based filtering yang dapat mempersonalisasi pengalaman pengguna dengan memberikan rekomendasi film sesuai preferensi individu. Sistem ini akan membantu pengguna menemukan film yang relevan dengan cepat dan efisien.

**2. Jawaban Pernyataan Masalah Kedua:** Mengembangkan model yang memanfaatkan metadata film secara optimal, seperti genre, sutradara, pemeran, dan durasi. Dengan menggunakan data ini, sistem dapat menghasilkan rekomendasi yang lebih relevan dengan tingkat presisi model di atas 75 persen.

**3. Jawaban Pernyataan Masalah Ketiga** Meningkatkan eksposur film lokal melalui rekomendasi yang didasarkan pada kesamaan atribut dengan film yang lebih populer. Dengan demikian, sistem ini dapat membantu memperkenalkan karya lokal kepada audiens yang lebih luas, sekaligus mendukung pertumbuhan industri film Indonesia.

Untuk mencapai tujuan dari proyek sistem rekomendasi berbasis content-based filtering, berikut adalah beberapa pendekatan solusi yang diusulkan:
1. **Pendekatan 1: Cosine Similarity**
Algoritma cosine similarity digunakan untuk menghitung kesamaan antar film berdasarkan atribut seperti genre, sutradara, dan pemeran. Pendekatan ini akan menghasilkan matriks kesamaan yang membantu dalam merekomendasikan film yang memiliki karakteristik serupa dengan film yang disukai pengguna.
Kelebihan dari metode ini adalah mudah diimplementasikan dan memberikan hasil yang cukup baik untuk data dengan dimensi tinggi. Sedangkan, kukurangnannya adalah kesamaan berbasis kata kunci saja dapat mengabaikan konteks semantik, misalnya kesamaan genre dalam skenario yang lebih kompleks.
2. **Pendekatan 2: TF-IDF Vectorization**
Term Frequency-Inverse Document Frequency (TF-IDF) digunakan untuk merepresentasikan data teks (genre, sutradara, aktor) sebagai vektor numerik. Dengan pendekatan ini, sistem dapat mengukur Term Frequency-Inverse Document Frequency (TF-IDF) digunakan untuk merepresentasikan data teks (genre, sutradara, aktor) sebagai vektor numerik. Dengan pendekatan ini, sistem dapat mengukur relevansi suatu film berdasarkan kata kunci unik yang dimilikinya, memperhitungkan frekuensi istilah di seluruh dataset.
Kelebihan metodr ini memperhitungkan pentingnya kata kunci spesifik dalam dataset, sehingga dapat mengurangi pengaruh kata umum. Kekurangannya tidak memperhitungkan hubungan semantik antara kata-kata, sehingga mungkin memerlukan penyesuaian tambahan.

## Data Understanding
Analisis ini berkaitan dengan perkembangan industri film di Indonesia pada periode 2000--2022 yang bersumber dari situs IMDb yang telah dikumpulkan oleh akun github atas nama [M. Irvan Dimetrio](https://github.com/IrvanDimetrio/IMDb-Movies-Analysis-in-Indonesia/blob/main/Data/Raw/imdb%20indonesia%20star.xlsx). Data tersebut disimpan dalam format excel yang sebelum dilakukan pra-pemrosesan data terdiri dari 2708 baris dan 12 kolom. Berikut ini merupakan rincian dan penjelasan mengenai kolom-kolom yeng terdapat dalam dataset ini.
1. **Title**: Judul film yang memberikan identifikasi utama untuk setiap entri dalam dataset.
2. **Year**: Tahun rilis film yang membantu mengelompokkan film berdasarkan periode waktu tertentu.
3. **Rated**: Kategori usia penonton yang disarankan untuk menonton film tersebut (misalnya, 13+, 18+, SU).
4. **Genre**: Jenis film berdasarkan kategori tematik, seperti drama, komedi, horor, dll.
5. **Runtime (Minutes)**: Durasi film dalam menit, memberikan informasi tentang panjang film.
6. **Rating**: Nilai rata-rata yang diberikan oleh pengguna, menggambarkan kualitas film secara keseluruhan.
7. **Votes**: Jumlah suara atau ulasan yang diterima oleh film, menunjukkan tingkat popularitas atau kepercayaan penonton.
8. **Director**: Nama sutradara film yang bertanggung jawab atas produksi dan arahan film.
9. **Star 1, Star 2, Star 3, Star 4**: Nama-nama pemeran utama dalam film, yang sering menjadi faktor penentu daya tarik film bagi penonton.

Penulisan data dalam dataset ini sudah terbilang cukup konsisten tetapi masih banyak baris yang kosong. Berikut ini perincian jumlah baris yang kosong setiap kolom beserta tipe data setiap kolom.

| No | Kolom              | Baris Kosong   | Tipe Data |
|----|--------------------|----------------|-----------|
| 1  | Title              | 0              | object    |
| 2  | Year               | 0              | int64     |
| 3  | Rated              | 0              | object    |
| 4  | Genre              | 0              | object    |
| 5  | Runtime (Minutes)  | 150            | object    |
| 6  | Rating             | 1133           | float64   |
| 7  | Votes              | 1133           | object    |
| 8  | Director           | 0              | object    |
| 9  | Star 1             | 238            | object    |
| 10 | Star 2             | 383            | object    |
| 11 | Star 3             | 568            | object    |
| 12 | Star 4             | 870            | object    |

Dari dataset di atas apabila dibuat menjadi sebuah visualisasi dan eksplorasi data sebelum dilakukan pra-pemrosesan data ternyata mendapatkan beberapa wawasan (insight) berikut ini.
1. Terdapat beberapa film yang frekuensi kemunculannya lebih dari sekali, sehingga perlu adanya pengolahan lebih lanjut. Hal ini seperti yang terlihat pada gambar di bawah ini.

![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Title.png?raw=true)

2. Setelah dilakukan ekplorasi data lebih lanjut ternyata diperoleh wawasan bahwa judul film yang muncul lebih dari sekali beberapa kolom secara tidak menentu memiliki nilai yang berbeda-beda. Hal ini seperti yang terlihat dalam tabel di bawah ini.

| No  | Title  | Year | Rated | Genre          | Runtime (Minutes) | Rating | Votes | Director            | Star 1                 | Star 2               | Star 3               | Star 4                     |
|-----|--------|------|-------|----------------|-------------------|--------|-------|---------------------|------------------------|----------------------|----------------------|----------------------------|
| 215 | Pulang | 2016 | 13+   | Short, Horror  | 4 min             | NaN    | NaN   | Kevin Anderson      | NaN                    | NaN                  | NaN                  | NaN                        |
| 297 | Pulang | 2021 | 13+   | Short, Family  | 19 min            | NaN    | NaN   | Wahyu Mika          | Adhelheid Bunga W.     | Bebe Gracia          | Watie Wibowo         | Hidayaturrahmat Al Lintawy |
| 460 | Pulang | 2021 | 13+   | Short, Drama   | 7 min             | NaN    | NaN   | Aldis Elwan         | Ananda Innaka Rahman   | NaN                  | NaN                  | NaN                        |
| 808 | Pulang | 2022 | R13+  | Drama, Romance | 84 min            | 8.5    | 6     | Azhar Kinoi Lubis   | Cok Simbara            | Ira Wibowo           | Dwi Sasono           | Della Dartyan              |
| 2190| Pulang | 2022 | R13+  | Drama          | 84 min            | 8.4    | 26    | Azhar Kinoi Lubis   | Ringgo Agus Rahman     | Ziva Magnolya        | Imelda Therinne      | Mark Natama                |

3. Setelah dibuat visualisasi data mendapatkan wawasan bahwa kolom nilai dalam kolom-kolom atribut film, yakni Year, Rated, Genre, Runtime (Minutes), Rating, Votes, Director, Star 1, Star 2, Star3, dan Star 4 memiliki frekuensi kemunculan yang berbeda-beda seperti yang terlihat dalam gambar di bawah ini. Sehingga jumlah kemunculan yang lebih sekali ini akan menjadi sebuah faktor kemiripan nilai antara film satu dengan yang lainnya.

![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Genre.png?raw=true)
![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Director.png?raw=true)
![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Star%201.png?raw=true)
![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Star%202.png?raw=true)
![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Star%203.png?raw=true)
![image alt](https://github.com/Suhardi100/Proyek-Akhir/blob/main/Visualisasi_Star%204.png?raw=true)

4. Setelah dilakukan eksplorasi dengan menampilkan statistik sederhana pada kolom-kolom numerik diketahui bahwa mayoritas film yang ada dalam dataset dirilis antara tahun 2012 dan 2023, dengan rating yang bervariasi antara 1.2 hingga 9.9. Rata-rata rating berada pada angka sekitar 6.43, yang menunjukkan bahwa film dalam dataset cenderung mendapatkan rating rata-rata yang cukup baik, meskipun ada beberapa film dengan rating yang lebih rendah.

| Statistik              | Tahun Rilis Film | Rating Film |
|------------------------|------------------|-------------|
| **Jumlah Data**        | 2708             | 1575        |
| **Rata-rata**          | 2015.30          | 6.43        |
| **Standar Deviasi**    | 5.14             | 1.55        |
| **Terendah (min)**     | 2000             | 1.2         |
| **Tertinggi (max)**    | 2023             | 9.9         |
| **Persentil 25%**      | 2012             | 5.6         |
| **Persentil 50%**      | 2016             | 6.6         |
| **Persentil 75%**      | 2019             | 7.4         |  

5. Setelah dilakukan ekplorasi data dengan pencarian baris dengan nilai duplikat diketahui bahwa terdapat sebanyak empat baris yang berisi nilai duplikat seperti di bawah ini.

| Title                                | Year | Rated | Genre          | Runtime (Minutes) | Rating | Votes | Director       | Star 1          | Star 2           | Star 3           | Star 4           |
|--------------------------------------|------|-------|----------------|-------------------|--------|-------|----------------|-----------------|------------------|------------------|------------------|
| Ingin Menunda: Would Like to Delay   | 2020 | 13+   | Short          | 4 min             | NaN    | NaN   | Alfa Kakauhe   | Alfa Kakauhe    | NaN              | NaN              | NaN              |
| Ingin Menunda: Would Like to Delay   | 2020 | 13+   | Short          | 4 min             | NaN    | NaN   | Alfa Kakauhe   | Alfa Kakauhe    | NaN              | NaN              | NaN              |
| The Mother's Land                    | 2020 | 13+   | Short, Fantasy | 25 min            | NaN    | NaN   | Kevin Rahardjo | Mikael Farady   | Sifra Magdalena  | NaN              | NaN              |
| The Mother's Land                    | 2020 | 13+   | Short, Fantasy | 25 min            | NaN    | NaN   | Kevin Rahardjo | Mikael Farady   | Sifra Magdalena  | NaN              | NaN              |

6. Setelah dilakukan ekplorasi data dengan menampilkan statistik sederhana pada kolom-kolom non-numerik diketahui bahwa film dengan judul "Pulang" muncul paling sering yakni sebanyak 5 kali dan sebagian besar film memiliki rating "13+" (1894 film). Genre yang paling umum adalah "Drama" dengan 417 film, sementara durasi film yang paling sering tercatat adalah "90 min" (162 film). Jumlah votes terbanyak adalah 7, menunjukkan sedikitnya ulasan atau penonton. Sutradara yang paling banyak mengarahkan film adalah Nayato Fio Nuala (70 film), sedangkan pemeran utama terbanyak adalah Reza Rahadian, yang muncul dalam 24 film. Adipati Dolken dan Donny Damara menduduki posisi kedua dan keempat sebagai pemeran terbanyak di posisi Star 2 dan Star 4.

| Statistik         | Title           | Rated | Genre | Runtime (Minutes) | Votes | Director            | Star 1            | Star 2              | Star 3             | Star 4            |
|-------------------|-----------------|-------|-------|-------------------|-------|---------------------|-------------------|---------------------|--------------------|-------------------|
| **Jumlah Data**   | 2708            | 2708  | 2708  | 2558              | 1575  | 2708                | 2470              | 2325                | 2140               | 1838              |
| **Unique Values** | 2681            | 20    | 275   | 154               | 391   | 1184                | 1550              | 1535                | 1490               | 1342              |
| **Nilai Teratas** | Pulang          | 13+   | Drama | 90 min            | 7     | Nayato Fio Nuala    | Reza Rahadian     | Adipati Dolken      | Reza Rahadian      | Donny Damara      |
| **Frekuensi**     | 5               | 1894  | 417   | 162               | 55    | 70                  | 24                | 15                  | 13                 | 9                 |

## Data Preparation
Pada proyek ini menerapkan beberapa teknik persiapan data untuk memastikan bahwa data yang digunakan untuk pemodelan bersih dan berkualitas. Teknik yang digunakan pada pada persiapan data pada proyek ini adalah sebagai berikut ini.

**1. Menghapus baris yang terdapat nilai yang duplikat**
Setelah didapatkan informasi pada tahap sebelumnya bahwa ada baris yang berisi nilai duplikat maka pada tahap ini akan dilakukan penghapusan. Penghapusan dilakukan dengan memanfaatkan fungsi library Pandas 'drop_duplicates()' yang secara default akan mempertahankan baris pertama dan menghapus baris berikutnya yang berisi nilai duplikat. Teknik ini penting dilakukan karena selain data duplikat tidak menambah informasi apapun, data ini juga akan memengaruhi model rekomendasi yang akan merekomendasikan baris duplikat tersebut karena memiliki kemiripan yang sempurna.

**2. Mengubah tipe data**
Tipe data pada kolom Runtime (Minutes) perlu diubah menjadi bertipe data float64 dengan cara menhapus kata "min" yang merupakan kependekan dari kata "minutes" lalu mengubahnya menjadi float64. Selain itu juga kolom votes juga perlu diubah menjadi float64 yang semula bertipe data sebagai object. Hal ini perlu dilakukan karena dalam kondisi nyata data tersebut tergolong data numerik yang harus diperlakukan sebagai sebuah angka bukan sebagai sebuah karakter atau string. Dengan begitu kolom-kolom tersebut bisa dilakukan pengolahan data lebih lanjut sebagai data yang bertipe numerik.

**3. Mengisi data pada baris yang kosong**
- Baris yang kosong pada kolom 'Runtime (Minutes)' diisi dengan nilai rata-rata. mengonversi kolom 'Runtime (Minutes)' menjadi tipe data float dan menghitung rata-rata dari nilai-nilai yang ada. Rata-rata ini digunakan untuk mengisi nilai yang kosong (NaN) di kolom tersebut. Fungsi fillna(mean_runtime) digunakan untuk menggantikan nilai kosong dengan rata-rata yang sudah dihitung.
- Baris yang kosong pada kolom 'Rating' diisi dengan nilai modus. Modus (nilai yang paling sering muncul) pada kolom 'Rating' dihitung menggunakan mode(). Jika ada lebih dari satu modus, yang pertama dipilih untuk mengisi nilai yang kosong. 
- Baris yang kosong pada kolom 'Votes' diisi dengan nilai modus. Sama seperti kolom 'Rating', kolom 'Votes' juga diisi dengan modusnya untuk menggantikan nilai kosong. 
Teknik ini penting untuk dilakukan untuk menghindari kehilangan data dan menjaga keutuhan informasi pada suatu kolom.

**4. Memilih atribut yang sesuai lalu menghapus baris yang berisi judul film yang frekuensi kemunculannya lebih dari sekali**
Pertama, data dikelompokkan berdasarkan kolom 'Title' menggunakan groupby('Title'), yang menghasilkan grup-grup film dengan judul yang sama. Selanjutnya, fungsi aggregate_data digunakan untuk mengolah setiap grup film, dengan memilih nilai tertentu seperti tahun rilis (mengambil tahun tertinggi), kategori rating (mengambil modus), genre (menggabungkan dan memilih modus), runtime, rating, jumlah suara (votes), serta aktor dan sutradara (menggunakan modus atau memilih nilai pertama jika modus tidak ada). Setelah itu, grouped.apply(aggregate_data) diterapkan untuk setiap grup. Teknik ini penting untuk dilakukan untuk menghindari suatu model merekomendasikan judul film yang sama dengan yang dicari.

**5. Menghapus kolom dan baris yang berisi nilai yang kosong**
- Kolom yang harus dihapus adalah kolom "Star 3" dan "Star 4" karena banyak mengandung baris yang kosong. Hal ini penting dilakukan karena kolom ini banyak mengandung data kosong dan apabila kita menghapus barisnya maka akan banyak kehilangan data. Sehingga yang perlu dihapus kolomnya.
- Baris yang harus dihapus adalah baris-baris yang masih mengandung nilai yang kosong pada beberapa kolom "Star 1" dan "Star 2". Hal ini penting untuk dilakukan karena kolom ini apabila kita hapus kolomnya juga maka akan kehilangan data penting berupa artis yang membintangi film tersebut, sehingga barisnya saja yang dihapus. Toh, tidak terlalu banyak baris yang harus dihapus untuk menghilangkan data yang kosong.   

**6. Menerapkan TF-IDF dalam ekstrasi fitur**
TF-IDF (Term Frequency-Inverse Document Frequency) adalah teknik statistik yang digunakan untuk mengevaluasi pentingnya sebuah kata dalam sebuah dokumen relatif terhadap kumpulan dokumen lainnya. Term Frequency (TF) mengukur seberapa sering sebuah kata muncul dalam dokumen, sedangkan Inverse Document Frequency (IDF) menurunkan bobot kata-kata umum yang sering muncul di seluruh dokumen tetapi tidak memiliki makna diskriminatif (misalnya, "dan," "adalah"). Dalam sistem rekomendasi, TF-IDF penting karena memungkinkan model memahami dan membandingkan dokumen atau item berdasarkan konten. 

Langkah-langkah yang dilakukan untuk mengekstrasi fitur dengan TF-IDF dalam proyek ini adalah sebagai berikut ini.
- Menggabungkan atribut dan menghitung TF-IDF. Mengabungkan atribut film (seperti genre, tahun, rating, dll.) menjadi satu daftar fitur kata unik, lalu menghitung skor TF-IDF untuk setiap kata agar mendapatkan representasi numerik berdasarkan frekuensinya dan tingkat kepentingannya. Ini membantu menangkap informasi penting dari semua atribut secara kolektif.
- Mengubah teks menjadi matriks TF-IDF. Mengubah data teks yang digabungkan tadi menjadi matriks TF-IDF yang merepresentasikan hubungan antara kata-kata unik dan dokumen. Proses ini mengubah teks menjadi format numerik untuk digunakan dalam model.
- Konversi ke matriks padat (dense). Mengubah matriks TF-IDF yang sparsed (banyak nilai nol) menjadi bentuk padat (dense matrix). Matriks padat lebih mudah digunakan dalam analisis lanjutan atau pemrosesan data lainnya.
- Mengonversi ke DataFrame. Transformasi matriks TF-IDF menjadi DataFrame untuk memudahkan eksplorasi, kemudian tampilkan sampel kecil untuk melihat isi data. Langkah ini membantu memahami hasil transformasi TF-IDF secara visual.

## Modeling
Model yang digunakan pada proyek ini adalah **Content Based Filtering**. Content Based Filtering adalah adalah teknik rekomendasi yang digunakan dalam sistem rekomendasi untuk menyarankan item kepada pengguna berdasarkan catatan interaksi terhadap atribut atau fitur dari suatu item oleh pengguna tersebut di masa lalu. 
Tahahapan dalam pembuatan model ini adalah sebagai berikut.
1. Menggunakan TfidfVectorizer untuk mengubah atribut-atribut film tertentu (seperti Year, Rated, Genre, Rating, Runtime, dll.) menjadi representasi numerik berdasarkan frekuensi kata dan kepentingannya, dengan cara menggabungkan semua atribut tersebut menjadi satu teks per baris, menghitung nilai TF-IDF, dan menghasilkan daftar fitur kata unik dari teks gabungan tersebut.
2. Mengubah data teks menjadi representasi matriks menggunakan teknik TF-IDF. 
3. Mengubah matriks sparse hasil dari TF-IDF menjadi matriks padat (dense matrix) sehingga lebih mudah dibaca dan diproses.
4. Mengonversi matriks TF-IDF menjadi DataFrame dan menampilkan sampel data secara acak untuk melihat subset yang lebih kecil dari matriks TF-IDF.
5. Menghitung cosine similarity antara setiap pasangan dokumen dalam matriks TF-IDF. Nilai similarity berada dalam rentang 0 hingga 1, di mana 1 menunjukkan dokumen yang identik dan 0 menunjukkan dokumen yang sangat berbeda. Hasilnya adalah matriks berbentuk persegi yang menunjukkan nilai cosine similarity antara setiap pasangan dokumen dalam dataset.
6. Membuat DataFrame yang memvisualisasikan matriks cosine similarity antara film-film berdasarkan fitur TF-IDF. Kemudian mengambil sampel secara acak untuk melihat sebagian kecil dari matriks similarity.
7. Memberikan rekomendasi film berdasarkan cosine similarity terhadap sebuah film yang diberikan. Dimulai dengan mencari indeks film yang paling mirip dengan film yang pernah ditonton oleh pengguna. Kemudian, mengambil film yang memiliki nilai similarity terbesar untuk direkomendasikan kepada pengguna.

Setelah melalui tahapan di atas, apabila pengguna pernah menonton film yang berjudul **Ziarah** maka akan direkomendasikan film-film berikut ini.
| Title                            | Year | Rated | Genre       | Rating | Runtime (Minutes)  | Votes | Director             | Star 1                    | Star 2                         |
|----------------------------------|------|-------|-------------|--------|--------------------|-------|----------------------|---------------------------|--------------------------------|
| Romantik Problematik             | 2022 | 17+   | Drama       | 7.2    | 86.0               | 7     | B.W. Purba Negara    | Bisma Karisma             | Lania Fira                     |
| Starting from A                  | 2011 | SU    | Short       | 8.6    | 16.0               | 22    | B.W. Purba Negara    | Bagus Suitrawan           | Natasya Putri Sastrosoemarto   |
| Doremi & You                     | 2019 | TV-G  | Drama       | 7.7    | 99.0               | 62    | B.W. Purba Negara    | Adyla Rafa Naura Ayu      | Devano Danendra                |
| 3600 Detik                       | 2014 | 13+   | Drama       | 6.7    | 90.0               | 46    | Nayato Fio Nuala     | Indra Birowo              | Ponco Buwono                   |
| Hantu Cantik Kok Ngompol         | 2016 | 13+   | Horror      | 7.2    | 78.0               | 7     | Emil G. Hampp        | Sarah Azhari              | Nana Mirdad                    |
| Kita punya bendera               | 2008 | SU    | Family      | 7.2    | 86.0               | 7     | Steven Purba         | Bima Anggara              | Nurul Hidayati                 |
| The Wedding Gift                 | 2013 | 13+   | Short       | 7.2    | 11.0               | 7     | Jason Iskandar       | Wijil Sinang Purba        | Anggita Swestiana              |
| Pantja Sila: Cita-Cita & Realita | 2016 | SU    | Documentary | 9.0    | 78.0               | 7     | Tyo Pakusadewo       | Tino Saroengallo          | Wicaksono Wisnu Legowo         |
| Banyu Biru                       | 2005 | 13+   | Drama       | 6.6    | 78.0               | 136   | Teddy Soeriaatmadja  | Tora Sudiro               | Dian Sastrowardoyo             |
| Belkibolang                      | 2011 | 13+   | Drama       | 5.9    | 87.0               | 25    | Edwin                | Ifa Isfansyah             | Azhar Kinoi Lubis              |

Adapun kelebihan dari model Content Based Filtering adalah sebagai berikut ini.
1. Rekomendasi didasarkan pada preferensi unik pengguna, sehingga lebih relevan dengan selera mereka.
2. Hanya membutuhkan data tentang film dan riwayat pengguna, sehingga cocok untuk sistem dengan sedikit pengguna aktif.
3. Dapat menghindari masalah cold start untuk item baru karena film baru dapat langsung direkomendasikan asalkan atributnya sudah ada di sistem.
4. Sistem dapat menjelaskan rekomendasinya (misalnya, "Film ini direkomendasikan karena Anda pernah menonton film aksi dengan aktor tertentu").
5. Independen terhadap popularitas, maksudnya adalah film dengan rating atau popularitas rendah tetap bisa direkomendasikan jika atributnya cocok dengan preferensi pengguna.
Sedangkan kekurangan dari model ini adalah sebagai berikut ini.
1. Untuk pengguna baru tanpa riwayat interaksi, sulit membangun profil awal, sehingga rekomendasi menjadi kurang akurat.
2. Over-Specialization, yakni sistem cenderung merekomendasikan film yang sangat mirip dengan yang sudah disukai, tanpa memperkenalkan variasi. Ini bisa membuat rekomendasi monoton.
3. Jika deskripsi film tidak cukup detail atau tidak mencakup semua aspek penting (misalnya tema atau nuansa emosional), sistem mungkin gagal mengenali kecocokan yang relevan.
4. Tidak Memanfaatkan Tren Sosial. Sistem ini tidak mempertimbangkan preferensi pengguna lain atau tren populer, sehingga mungkin tidak merekomendasikan film yang sedang banyak dibicarakan.
5. Kesulitan dalam Mengukur Aspek Subjektif. Preferensi pengguna terhadap elemen yang subjektif seperti humor atau plot twist sulit direpresentasikan dengan atribut film.

## Evaluation

Apabila pengguna pernah menonton film yang berjudul **Ziarah** dengan atribut berikut ini.

| Title   | Year | Rated | Genre | Runtime (Minutes)  | Rating | Votes | Director          | Star 1         | Star 2        |
|---------|------|-------|-------|--------------------|--------|-------|-------------------|----------------|---------------|
| Ziarah  | 2016 | 13+   | Drama | 87.0               | 8.3    | 78    | B.W. Purba Negara | Ponco Sutiyem  | Rukman Rosadi |

Maka akan direkomendasikan untuk menonton film-film dengan judul dan atribut berikut ini.

| Title                            | Year | Rated | Genre       | Rating | Runtime (Minutes)  | Votes | Director             | Star 1                    | Star 2                         |
|----------------------------------|------|-------|-------------|--------|--------------------|-------|----------------------|---------------------------|--------------------------------|
| Romantik Problematik             | 2022 | 17+   | Drama       | 7.2    | 86.0               | 7     | B.W. Purba Negara    | Bisma Karisma             | Lania Fira                     |
| Starting from A                  | 2011 | SU    | Short       | 8.6    | 16.0               | 22    | B.W. Purba Negara    | Bagus Suitrawan           | Natasya Putri Sastrosoemarto   |
| Doremi & You                     | 2019 | TV-G  | Drama       | 7.7    | 99.0               | 62    | B.W. Purba Negara    | Adyla Rafa Naura Ayu      | Devano Danendra                |
| 3600 Detik                       | 2014 | 13+   | Drama       | 6.7    | 90.0               | 46    | Nayato Fio Nuala     | Indra Birowo              | Ponco Buwono                   |
| Hantu Cantik Kok Ngompol         | 2016 | 13+   | Horror      | 7.2    | 78.0               | 7     | Emil G. Hampp        | Sarah Azhari              | Nana Mirdad                    |
| Kita punya bendera               | 2008 | SU    | Family      | 7.2    | 86.0               | 7     | Steven Purba         | Bima Anggara              | Nurul Hidayati                 |
| The Wedding Gift                 | 2013 | 13+   | Short       | 7.2    | 11.0               | 7     | Jason Iskandar       | Wijil Sinang Purba        | Anggita Swestiana              |
| Pantja Sila: Cita-Cita & Realita | 2016 | SU    | Documentary | 9.0    | 78.0               | 7     | Tyo Pakusadewo       | Tino Saroengallo          | Wicaksono Wisnu Legowo         |
| Banyu Biru                       | 2005 | 13+   | Drama       | 6.6    | 78.0               | 136   | Teddy Soeriaatmadja  | Tora Sudiro               | Dian Sastrowardoyo             |
| Belkibolang                      | 2011 | 13+   | Drama       | 5.9    | 87.0               | 25    | Edwin                | Ifa Isfansyah             | Azhar Kinoi Lubis              |

Rekomendasi di atas menjawab **permasalahan pertama**, yakni **pengguna tidak lagi merasa kesulitan menemukan film yang sesuai dengan preferensi mereka di tengah ribuan pilihan yang tersedia di platform streaming.**

Selanjutnya hasil di atas akan dievaluasi dengan matriks **Precision**. Berikut ini merupakan hasil dari evaluasi menggunakan matriks precision tersebut.

| Title                                 | Kesesuaian Pertama               | Kesesuaian Kedua               | Jumlah Kecocokan |
|---------------------------------------|----------------------------------|--------------------------------|------------------|
| **Romantik Problematik**              | Genre (Drama)                    | Tidak ada atribut yang cocok   | 1 atribut        |
| **Starting from A**                   | Director (B.W. Purba Negara)     | Tidak ada atribut yang cocok   | 1 atribut        |
| **Doremi & You**                      | Genre (Drama)                    | Director (B.W. Purba Negara)   | 2 atribut        |
| **3600 Detik**                        | Genre (Drama)                    | Rated (13+)                    | 2 atribut        |
| **Hantu Cantik Kok Ngompol**          | Rated (13+)                      | Tidak ada atribut yang cocok   | 1 atribut        |
| **Kita Punya Bendera**                | Tidak ada atribut yang cocok     | Tidak ada atribut yang cocok   | 0 atribut        |
| **The Wedding Gift**                  | Rated (13+)                      | Tidak ada atribut yang cocok   | 1 atribut        |
| **Pantja Sila: Cita-Cita & Realita**  | Tidak ada atribut yang cocok     | Tidak ada atribut yang cocok   | 0 atribut        |
| **Banyu Biru**                        | Genre (Drama)                    | Rated (13+)                    | 2 atribut        |
| **Belkibolang**                       | Genre (Drama)                    | Rated (13+)                    | 2 atribut        |

Apabila kita menerapkan ambang batas satu kecocokan sudah dikatakan relevan maka ada 8 film yang relevan dan 2 film tidak relevan. Dengan begitu nilai presisi model ini sebesar **80 persen**.

Hasil evaluasi di atas menjawab **permasalahan kedua**, yakni **model yang memanfaatkan metadata film secara optimal dengan nilai presisi model di atas 75 persen.**

Hasil di atas juga memuat film-film lokal yang kurang populer, seperti Hantu Cantik Kok Ngompol, Banyu Biru, dan Belkibolang. Sehingga hasil rekomendasi di atas menjawab **permasalahan ketiga**, yakni **Film-film lokal, terutama yang memiliki nilai seni tinggi tetapi kurang populer, sudah terekspos dengan baik kepada para pengguna.**

