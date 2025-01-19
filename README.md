# 🔑 Password Cracking Using Brute Force

## **Deskripsi Proyek**
Proyek ini merupakan implementasi dari metode brute force untuk memecahkan password secara sistematis. Brute force adalah salah satu metode eksplorasi kombinasi karakter yang memungkinkan untuk menemukan password dengan cara mencoba setiap kemungkinan karakter satu per satu hingga password yang benar ditemukan. 

Proyek ini dibuat sebagai bagian dari mini project untuk mata kuliah **Kompleksitas Algoritma**. Metode ini menggambarkan proses pencarian secara menyeluruh, sehingga menjadi contoh klasik algoritma dengan kompleksitas eksponensial.

Proyek ini dikerjakan oleh kelompok dengan anggota:
- Raffi Putra
- Alfredo Alin Kambu
- Siti Fauzziyah
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

## **Implementasi Program**

Berikut adalah kode Python untuk implementasi metode brute force dalam memecahkan password:

```python
import itertools
import string
import time

def brute_force_password_cracking(target_password):
    """
    Attempts to crack the given password using brute force.
    
    Parameters:
    - target_password (str): The password to be cracked.
    
    Returns:
    - cracked_password (str): The successfully cracked password.
    - attempts (int): The number of attempts it took to crack the password.
    - elapsed_time (float): The time taken in seconds to crack the password.
    """
    # gunakan huruf kecil untuk mempercepat proses
    charset = string.ascii_lowercase
    max_length = len(target_password) 

    attempts = 0  
    start_time = time.time()  # Waktu mulai

    print("Starting brute force password cracking...")

    # Langsung fokus pada panjang password target
    for length in range(max_length, max_length + 1):
        print(f"Trying passwords of length {length}...")

        # Menghasilkan semua kombinasi
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1  # Increment jumlah percobaan
            
            # Menggabungkan tuple menjadi string
            attempted_password = ''.join(attempt)

            # Menampilkan progres (opsional)
            if attempts % 1000000 == 0:  # Cetak progres setiap 1 juta percobaan
                print(f"Attempts: {attempts} - Current Password: {attempted_password}")

            # Jika password cocok
            if attempted_password == target_password:
                elapsed_time = time.time() - start_time  # Hitung waktu total
                print("Password cracked successfully!")
                return attempted_password, attempts, elapsed_time

    # Jika tidak ditemukan
    print("Failed to crack the password.")
    return None, attempts, None


# Contoh
if __name__ == "__main__":
    # Target password
    target_password = "fathir"

    # Memulai proses brute force
    cracked_password, attempts, elapsed_time = brute_force_password_cracking(target_password)

    # hasil
    if cracked_password:
        print(f"Cracked Password: {cracked_password}")
        print(f"Number of Attempts: {attempts}")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
    else:
        print(f"Failed after {attempts} attempts.")


```

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

