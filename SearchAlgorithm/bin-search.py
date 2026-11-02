def binary_search(array: list[int], target: int) -> int:
    """Fungsi modul 1: Melakukan pencarian biner pada list yang sudah terurut.

    Mengembalikan indeks target jika ditemukan, atau -1 jika tidak ditemukan.
    """
    kiri = 0
    kanan = len(array) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        # Cek apakah elemen tengah adalah target
        if array[tengah] == target:
            return tengah

        # Jika target lebih besar, abaikan bagian kiri
        if array[tengah] < target:
            kiri = tengah + 1
        # Jika target lebih kecil, abaikan bagian kanan
        else:
            kanan = tengah - 1

    return -1


def siapkan_data(panjang_data: int) -> list[int]:
    """Fungsi modul 2: Menyiapkan dan mengurutkan data angka."""
    # Data harus dalam kondisi terurut untuk Binary Search
    data = [x * 2 for x in range(panjang_data)]
    return data


def tampilkan_laporan(target: int, indeks: int, data: list[int]) -> None:
    """Fungsi modul 3: Format pencetakan hasil pencarian ke layar."""
    print("=" * 45)
    print("HASIL PENCARIAN BINARY SEARCH")
    print("=" * 45)
    print(f"Data Sampel (5 pertama) : {data[:5]} ...")
    print(f"Target yang dicari       : {target}")

    if indeks != -1:
        print(f"Status                  : Ditemukan!")
        print(f"Posisi Indeks           : {indeks}")
    else:
        print(f"Status                  : Tidak Ditemukan dalam data.")
    print("=" * 45)


def main():
    """Fungsi Utama (Entry Point) untuk mengatur alur program."""
    # 1. Olah data
    data_angka = siapkan_data(100)
    target_cari = 42

    # 2. Eksekusi pencarian
    hasil_indeks = binary_search(data_angka, target_cari)

    # 3. Tampilkan hasil
    tampilkan_laporan(target_cari, hasil_indeks, data_angka)


if __name__ == "__main__":
    main()
