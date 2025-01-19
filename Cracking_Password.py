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
    target_password = "adeliasabira"

    # Memulai proses brute force
    cracked_password, attempts, elapsed_time = brute_force_password_cracking(target_password)

    # hasil
    if cracked_password:
        print(f"Cracked Password: {cracked_password}")
        print(f"Number of Attempts: {attempts}")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
    else:
        print(f"Failed after {attempts} attempts.")

