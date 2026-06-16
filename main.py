# 1. Import pustaka yang dibutuhkan
import cv2 as cv

# 2. Membaca file gambar dari lokasi yang kamu tentukan di dalam tanda kutip
img = cv.imread("...")

# 3. Mengimpor fungsi khusus dari Google Colab untuk menampilkan gambar ke layar,
# lalu memanggil fungsi tersebut untuk menampilkan gambar asli yang ada di variabel 'img'.
from google.colab.patches import cv2_imshow
cv2_imshow(img)

# 4. Menerapkan operator Laplacian pada gambar 'img' dan menyimpan hasilnya dalam format 8-bit (cv.CV_8U), 
# lalu masukkan hasilnya ke dalam variabel bernama 'edge'."
edge = cv.Laplacian(img,cv.CV_8U)
cv2_imshow(edge)


# 5. cv.threshold menghasilkan dua nilai: batas yang dipakai (thresh) dan gambar hasilnya (blackAndWhite)
(thresh, blackAndWhite) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv2_imshow(blackAndWhite)
