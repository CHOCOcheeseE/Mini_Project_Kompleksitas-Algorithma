# 🔑 Password Cracking Using Brute Force

## **Deskripsi Proyek**
Proyek ini merupakan implementasi dari metode brute force untuk memecahkan password secara sistematis. Brute force adalah salah satu metode eksplorasi kombinasi karakter yang memungkinkan untuk menemukan password dengan cara mencoba setiap kemungkinan karakter satu per satu hingga password yang benar ditemukan. 

Proyek ini dibuat sebagai bagian dari mini project untuk mata kuliah **Kompleksitas Algoritma**. Metode ini menggambarkan proses pencarian secara menyeluruh, sehingga menjadi contoh klasik algoritma dengan kompleksitas eksponensial.

Proyek ini dikerjakan oleh kelompok dengan anggota:
- Raffi Putra
- Alfredo Alin Kambu
- Siti Fauziyah
- Adelia Sabira
- Muhammad Fathir Bagas

---

## **Tujuan Proyek**
1. Memahami cara kerja metode brute force pada kasus nyata, yaitu password cracking.
2. Mengukur kompleksitas waktu algoritma brute force berdasarkan panjang password dan ukuran charset.
3. Memberikan wawasan tentang pentingnya keamanan password dengan menggunakan kombinasi panjang dan kompleksitas karakter.

---

## **Fitur Utama**
- **Charset Lengkap:** Program mendukung kombinasi karakter berikut:
  - Huruf kecil (`a-z`)
  - Huruf besar (`A-Z`)
  - Angka (`0-9`)
  - Simbol spesial (seperti `!@#$%^&*()` dan lainnya)
- **Progres Real-Time:** Program menampilkan percobaan password secara berkala untuk memberikan informasi proses yang sedang berjalan.
- **Panjang Password Maksimal:** Program mendukung panjang password hingga **8 karakter**.
- **Output Lengkap:** Program menampilkan hasil akhir berupa password yang ditemukan, jumlah percobaan, dan waktu eksekusi.

---

## **Cara Kerja Program**
1. **Input:**
   - Program meminta pengguna memasukkan password yang ingin dipecahkan.
   - Panjang password maksimal adalah 8 karakter.
2. **Proses:**
   - Program mulai mencoba kombinasi karakter dari panjang 1 hingga panjang maksimal yang ditentukan.
   - Untuk setiap panjang, semua kemungkinan kombinasi karakter akan dicoba secara sistematis hingga menemukan kecocokan.
3. **Output:**
   - Setelah password ditemukan, program akan menampilkan:
     - Password yang berhasil dipecahkan.
     - Jumlah total percobaan yang dilakukan.
     - Waktu yang diperlukan untuk menemukan password tersebut.

---

## **Teknologi yang Digunakan**
- **Bahasa Pemrograman:** Python 3
- **Pustaka Python:**
  - `itertools`: Digunakan untuk menghasilkan kombinasi karakter.
  - `string`: Digunakan untuk mendefinisikan charset (karakter yang akan digunakan).
  - `time`: Digunakan untuk menghitung durasi eksekusi program.

---

## **Penjelasan Contoh Output**
### **Input**
- Password target yang dimasukkan: `fathir` (6 karakter).

### **Proses**
- Program mencoba semua kemungkinan kombinasi mulai dari panjang 1 hingga 6 dengan charset lengkap.
- Kombinasi terakhir sebelum menemukan password adalah `ezcwt` (hanya ditampilkan sebagai progres).

### **Output**
- Password berhasil ditemukan: `fathir`.
- Jumlah percobaan yang dilakukan: **59.745.782 percobaan**.
- Waktu yang diperlukan: **13,76 detik**.

---

## **Analisis Kompleksitas**
1. **Kompleksitas Waktu:**
   - Kompleksitas brute force adalah **O(C^L)**, di mana:
     - `C` adalah ukuran charset (jumlah karakter yang digunakan).
     - `L` adalah panjang password.
   - Pada contoh ini:
     - Ukuran charset: 94 (karakter ASCII dari `string.printable`).
     - Panjang password: 6.
     - Kombinasi total = 94^6 = 689.869.781.056.

2. **Efisiensi:**
   - Metode ini **tidak efisien** untuk panjang password besar atau charset yang luas karena jumlah kombinasi bertambah secara eksponensial.

---

## **Keunggulan dan Keterbatasan**

### **Keunggulan:**
- **Fleksibilitas:** Mendukung berbagai jenis karakter dalam charset.
- **Progres Real-Time:** Menampilkan progres setiap 1 juta percobaan.
- **Implementasi Sederhana:** Menggunakan pustaka bawaan Python.

### **Keterbatasan:**
- **Waktu Eksekusi:** Lama untuk password panjang atau charset besar.
- **Tidak Efisien:** Kompleksitas eksponensial membuat brute force tidak praktis untuk password yang kuat.

---

## **Rekomendasi untuk Keamanan Password**
1. **Gunakan Password Panjang:**
   - Pilih password dengan panjang minimal **12 karakter**.
2. **Gunakan Kombinasi Karakter:**
   - Kombinasikan huruf besar, huruf kecil, angka, dan simbol.
3. **Hindari Pola Sederhana:**
   - Jangan gunakan pola yang mudah ditebak, seperti `123456` atau `password`.
4. **Gunakan Sistem Pendukung Keamanan:**
   - Implementasikan mekanisme seperti **rate limiting** atau **lockout** untuk mencegah serangan brute force.

---

## **Pengembangan Selanjutnya**
1. **Optimasi Performa:**
   - Gunakan paralelisme dengan pustaka seperti `multiprocessing` untuk mencoba kombinasi secara paralel.
2. **Dukungan GPU:**
   - Manfaatkan GPU untuk meningkatkan kecepatan brute force dengan pustaka seperti CUDA atau OpenCL.
3. **Pemanfaatan Sistem Distribusi:**
   - Sebarkan proses brute force ke beberapa komputer untuk meningkatkan skala dan kecepatan.

---

## **Lisensi**
Proyek ini dirilis di bawah lisensi **MIT**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan proyek ini dengan tetap mematuhi ketentuan lisensi.

---

Jika ada pertanyaan atau saran terkait proyek ini, jangan ragu untuk membuka **issue** atau membuat **pull request** di repositori ini. Terima kasih!

