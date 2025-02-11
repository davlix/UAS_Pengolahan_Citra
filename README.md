# Deteksi Tepi dan Segmentasi Citra dengan Python

## Deskripsi
Repositori ini berisi implementasi deteksi tepi dan segmentasi citra menggunakan berbagai metode dalam pengolahan citra digital. Teknik ini sangat penting dalam berbagai aplikasi visi komputer seperti segmentasi gambar, pengenalan objek, dan pemrosesan medis. Metode yang digunakan dalam proyek ini meliputi:

### **Deteksi Tepi**
- **Operator Roberts**: Deteksi tepi cepat tetapi sangat sensitif terhadap noise.
- **Operator Sobel**: Deteksi tepi dengan filter yang lebih besar sehingga hasilnya lebih halus dibanding Roberts.
- **Operator Prewitt**: Mirip dengan Sobel, tetapi lebih sensitif terhadap perubahan orientasi.
- **Deteksi Tepi Canny**: Metode yang lebih kompleks dengan beberapa tahapan, termasuk perataan Gaussian, gradien Sobel, non-maximum suppression, dan hysteresis thresholding.

### **Segmentasi Citra**
- **K-Means Clustering**: Teknik pengelompokan piksel berdasarkan kesamaan warna atau intensitas untuk membagi gambar menjadi beberapa bagian.

Kode ini ditulis menggunakan **Python** dengan pustaka **NumPy, OpenCV, SciPy, dan Matplotlib**.

## Instalasi
Untuk menjalankan kode ini, pastikan Anda memiliki Python dan pustaka yang dibutuhkan. Gunakan perintah berikut untuk menginstalnya:
```bash
pip install numpy imageio opencv-python scipy matplotlib
```

## Penggunaan
1. Jalankan skrip Python dalam **Google Colab** atau lokal.
2. Unggah gambar yang ingin diproses melalui input file.
3. Program akan memproses gambar menggunakan berbagai metode deteksi tepi dan segmentasi citra.
4. Hasilnya akan ditampilkan dalam bentuk visualisasi perbandingan.

## Implementasi Teknis
### Deteksi Tepi
#### Operator Roberts
Operator Roberts menggunakan dua kernel kecil untuk menghitung gradien dalam arah diagonal:
```python
roberts_x = np.array([[1, 0], [0, -1]])
roberts_y = np.array([[0, 1], [-1, 0]])
```

#### Operator Sobel
Sobel menggunakan dua kernel yang lebih besar untuk mendeteksi perubahan intensitas:
```python
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
```

#### Operator Prewitt
Prewitt mirip dengan Sobel tetapi bobotnya lebih sederhana:
```python
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
```

#### Deteksi Tepi Canny
Deteksi tepi Canny terdiri dari beberapa tahap:
1. Gaussian Blur untuk mengurangi noise.
2. Deteksi gradien dengan operator Sobel.
3. Non-maximum suppression untuk menghilangkan tepi palsu.
4. Hysteresis thresholding untuk mendapatkan tepi yang jelas.

### **Segmentasi Citra dengan K-Means**
Segmentasi citra menggunakan **K-Means Clustering** bertujuan untuk membagi gambar menjadi beberapa bagian berdasarkan kesamaan warna atau intensitas pikselnya.

#### Implementasi K-Means Clustering:

## Analisis dan Perbandingan
Dari hasil deteksi tepi dan segmentasi, diperoleh beberapa kesimpulan:
1. **Operator Roberts**: Cepat tetapi lebih sensitif terhadap noise, sehingga kurang cocok untuk gambar dengan banyak detail halus.
2. **Operator Sobel**: Menghasilkan deteksi yang lebih halus dan lebih baik untuk menangkap tepi yang lebih lebar.
3. **Operator Prewitt**: Mirip dengan Sobel tetapi memiliki performa lebih baik pada orientasi vertikal dan horizontal.
4. **Deteksi Tepi Canny**: Metode terbaik dengan ketahanan terhadap noise dan deteksi tepi yang lebih akurat berkat proses multi-tahapnya.
5. **Segmentasi K-Means**: Mengelompokkan piksel berdasarkan warna, sehingga dapat digunakan untuk pemisahan objek atau pemrosesan lebih lanjut dalam analisis gambar.

## Hasil Visualisasi
Berikut adalah contoh hasil deteksi tepi :

![Screenshot 2025-02-11 224704](https://github.com/user-attachments/assets/ee8ec205-b398-4838-9daa-34f6d095b8c9)

Berikut adalah contoh hasil deteksi Segmentasi K-Means dengan 4 Klaste :

![Screenshot 2025-02-11 230225](https://github.com/user-attachments/assets/73a669f1-64bc-45f7-81d2-b9cf2ed951db)


- **Gambar Asli**
- **Deteksi Tepi Roberts**
- **Deteksi Tepi Sobel**
- **Deteksi Tepi Prewitt**
- **Deteksi Tepi Canny**
- **Segmentasi K-Means dengan 4 Klaster**

Hasil menunjukkan bahwa **Canny Edge Detection** memberikan hasil terbaik dalam hal kejelasan dan akurasi, sedangkan **Segmentasi K-Means** efektif dalam membagi gambar menjadi beberapa area berdasarkan warna.

## Aplikasi dan Penggunaan Lebih Lanjut
Deteksi tepi dan segmentasi citra memiliki banyak aplikasi dalam dunia nyata, seperti:
- Pengenalan objek dalam citra medis.
- Pengenalan pola dalam citra satelit.
- Pembuatan filter efek visual dalam bidang seni digital.
- Peningkatan sistem navigasi dalam kendaraan otonom.
- Pemrosesan citra untuk analisis produk dalam industri manufaktur.



