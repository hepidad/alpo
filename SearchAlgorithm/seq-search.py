def sequential_search(array: list[int], target: int) -> int:
    """Fungsi modul 1: Melakukan pencarian linier elemen demi elemen.
    
    Mengembalikan indeks target jika ditemukan, atau -1 jika tidak ditemukan.
    """
    for indeks in range(len(array)):
        if array[indeks] == target:
            return indeks  # Target ditemukan, kembalikan posisi indeksnya
            
    return -1  # Target tidak ditemukan setelah memeriksa seluruh elemen


def siapkan_data() -> list[int]:
    """Fungsi modul 2: Menyiapkan data acak (tidak perlu terurut)."""
    return [42, 15, 88, 7, 23, 99, 54, 12]


def tampilkan_laporan(target: int, indeks: int, data: list[int]) -> None:
    """Fungsi modul 3: Format pencetakan hasil pencarian ke layar."""
    print("=" * 45)
    print("HASIL PENCARIAN SEQUENTIAL SEARCH")
    print("=" * 45)
    print(f"Data Acak         : {data}")
    print(f"Target yang dicari: {target}")
    
    if indeks != -1:
        print(f"Status            : Ditemukan!")
        print(f"Posisi Indeks     : {indeks}")
    else:
        print(f"Status            : Tidak Ditemukan dalam data.")
    print("=" * 45)


def main():
    """Fungsi Utama (Entry Point) untuk mengatur alur eksekusi."""
    # 1. Inisialisasi data
    data_angka = siapkan_data()
    target_cari = 23
    
    # 2. Jalankan pencarian
    hasil_indeks = sequential_search(data_angka, target_cari)
    
    # 3. Tampilkan hasil
    tampilkan_laporan(target_cari, hasil_indeks, data_angka)


if __name__ == "__main__":
    main()
