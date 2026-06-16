# Komputer-Vision-Binary-Image-
- **Binary Image** merupakan jenis citra yang lebih sederhana lagi dari grayscale, di mana hanya ada dua kemungkinan nilai piksel: 0 (Hitam) atau 1/255 (Putih)
- **Bagaimana membuatnya ?** Menggunakan teknik thresholding (ambang batas). Kita menentukan satu nilai threshold, misalnya 127. Semua piksel di citra grayscale yang nilainya lebih besar dari 127 akan diubah menjadi putih, sedangkan yang di bawah atau sama dengan 127 akan diubah menjadi hitam
- **Fungsi Utama :** teknik ini memisahkan objek utama (foreground) dengan mulus dari latar belakang (background) sehingga mesin hanya fokus pada siluet objek

# Langkah-Langkah
Berikut adalah panduan langkah demi langkah untuk mengubah gambar menjadi binary menggunakan Python di Google Colab. Kita akan menggunakan pustaka **OpenCV**, yang merupakan standar industri untuk Computer Vision.

### 1️⃣ Masuk Google Colab
- Buka browser dan masuk ke Google Colab
- Klik New Notebook untuk membuat lembar kerja baru

### 2️⃣ Unggah Gambar
Sebelum mengeksekusi kode, kita perlu memasukkan gambar ke dalam sistem penyimpanan seperti Google Drive atau Colab. Contoh di sini menggunakan gambar bunga dahlia
<img width="593" height="376" alt="image" src="https://github.com/user-attachments/assets/ebedd707-7581-4e74-b979-140d051e2d54" />

➡️ Setelah mengunggah gambar, lakukan **mount drive** untuk menghubungkan Colab dengan Google Drive milik kalian
<img width="1832" height="1479" alt="Asset 11" src="https://github.com/user-attachments/assets/047273fc-9a46-4e57-922d-9ae8c4f89ce1" />

### 3️⃣ Mengimport CV
<img width="926" height="332" alt="image" src="https://github.com/user-attachments/assets/e855a52c-2994-45ff-8c78-7c6ae60ee8f3" />

Keterangan :
- Kode pada sel pertama digunakan untuk mengimport pustaka
- Kode pada sel kedua digunakan untuk membaca gambar yang telah diunggah ke Google Drive
  
  : ⚠️ pastikan tempat penyimpanan ("...") sesuai dengan tempat kalian upload
  
  : ⚠️ atau kalian bisa cari gambar kemudian klik titik tiga (⋮) pilih "Copy path", kemudian paste ke ("...")
- Kode pada sel ketiga digunakan menampilkan gambar

### 4️⃣ Mengubah warna menjadi Binary
<img width="523" height="358" alt="Screenshot 2026-06-16 132024" src="https://github.com/user-attachments/assets/96b208af-98ed-46f0-8d9e-2aa30868d512" />

Keterangan :
- Kode pada sel keempat digunakan mengkonversi gambar dari BGR ke Grayscale dan tampilkan hasil gambar
