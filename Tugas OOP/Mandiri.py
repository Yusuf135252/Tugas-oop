class Kasir:
    def __init__(self, nama_barang, harga, jumlah):
        self.nama_barang = nama_barang
        self.harga = harga
        self.jumlah = jumlah
        self.total = 0

    def tambah_barang(self):
        print("Barang ditambahkan:", self.nama_barang)

    def hitung_total(self):
        self.total = self.harga * self.jumlah
        return self.total

    def info_transaksi(self):
        print("Nama barang:", self.nama_barang)
        print("Harga:", self.harga)
        print("Jumlah:", self.jumlah)
        print("Total harga:", self.hitung_total())


# Instansiasi objek
barang1 = Kasir("Buku", 5000, 3)

barang1.tambah_barang()
barang1.info_transaksi()
